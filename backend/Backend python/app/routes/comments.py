from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from typing import List, Optional
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/api/comments", tags=["comments"])

# GET - Todos los comentarios con filtros
@router.get("/", response_model=schemas.CommentList)
def get_comments(
    skip: int = 0,
    limit: int = 50,
    page_section: Optional[str] = Query(None, description="Filtrar por sección"),
    post_id: Optional[int] = Query(None, description="Filtrar por post ID"),
    approved_only: bool = Query(True, description="Solo comentarios aprobados"),
    include_replies: bool = Query(False, description="Incluir respuestas"),
    sort_by: str = Query("newest", description="Ordenar por: newest, oldest, rating"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Comment)
    
    # Filtrar por aprobación
    if approved_only:
        query = query.filter(models.Comment.is_approved == True)
    
    # Filtrar por sección
    if page_section:
        query = query.filter(models.Comment.page_section == page_section)
    
    # Filtrar por post
    if post_id:
        query = query.filter(models.Comment.post_id == post_id)
    
    # Filtrar solo comentarios padres (no respuestas)
    if not include_replies:
        query = query.filter(models.Comment.parent_id.is_(None))
    
    # Ordenar
    if sort_by == "newest":
        query = query.order_by(desc(models.Comment.created_at))
    elif sort_by == "oldest":
        query = query.order_by(models.Comment.created_at)
    elif sort_by == "rating":
        query = query.order_by(desc(models.Comment.rating))
    
    total_count = query.count()
    comments = query.offset(skip).limit(limit).all()
    
    # Contar respuestas para cada comentario
    for comment in comments:
        comment.reply_count = db.query(models.Comment).filter(
            models.Comment.parent_id == comment.id,
            models.Comment.is_approved == True
        ).count()
    
    return {
        "success": True,
        "count": len(comments),
        "total_count": total_count,
        "data": comments
    }

# GET - Comentario por ID
@router.get("/{comment_id}", response_model=schemas.CommentWithReplies)
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    
    if not comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    
    # Obtener respuestas
    replies = db.query(models.Comment).filter(
        models.Comment.parent_id == comment_id,
        models.Comment.is_approved == True
    ).order_by(models.Comment.created_at).all()
    
    comment.replies = replies
    comment.reply_count = len(replies)
    
    return comment

# POST - Crear nuevo comentario
@router.post("/", response_model=schemas.OperationResponse)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    # Verificar si el comentario padre existe
    if comment.parent_id:
        parent_comment = db.query(models.Comment).filter(
            models.Comment.id == comment.parent_id
        ).first()
        if not parent_comment:
            raise HTTPException(status_code=404, detail="Comentario padre no encontrado")
    
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    
    return {
        "success": True,
        "message": "Comentario creado exitosamente. Está pendiente de aprobación.",
        "comment_id": db_comment.id
    }

# PUT - Actualizar comentario
@router.put("/{comment_id}", response_model=schemas.OperationResponse)
def update_comment(comment_id: int, comment_update: schemas.CommentUpdate, db: Session = Depends(get_db)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    
    update_data = comment_update.dict(exclude_unset=True)
    
    # Marcar como editado si se cambia el contenido
    if 'content' in update_data and update_data['content'] != db_comment.content:
        update_data['is_edited'] = True
        update_data['edited_at'] = func.now()
    
    for field, value in update_data.items():
        setattr(db_comment, field, value)
    
    db.commit()
    
    return {
        "success": True,
        "message": "Comentario actualizado exitosamente",
        "comment_id": db_comment.id
    }

# DELETE - Eliminar comentario
@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    
    # Eliminar también las respuestas si las hay
    db.query(models.Comment).filter(models.Comment.parent_id == comment_id).delete()
    db.delete(db_comment)
    db.commit()
    
    return {
        "success": True,
        "message": "Comentario y sus respuestas eliminados exitosamente"
    }

# GET - Comentarios por sección
@router.get("/section/{page_section}", response_model=schemas.CommentList)
def get_comments_by_section(
    page_section: str,
    skip: int = 0,
    limit: int = 50,
    approved_only: bool = True,
    db: Session = Depends(get_db)
):
    query = db.query(models.Comment).filter(models.Comment.page_section == page_section)
    
    if approved_only:
        query = query.filter(models.Comment.is_approved == True)
    
    query = query.filter(models.Comment.parent_id.is_(None))
    query = query.order_by(desc(models.Comment.created_at))
    
    total_count = query.count()
    comments = query.offset(skip).limit(limit).all()
    
    # Contar respuestas
    for comment in comments:
        comment.reply_count = db.query(models.Comment).filter(
            models.Comment.parent_id == comment.id,
            models.Comment.is_approved == True
        ).count()
    
    return {
        "success": True,
        "count": len(comments),
        "total_count": total_count,
        "data": comments
    }

# GET - Estadísticas de comentarios
@router.get("/stats/summary", response_model=schemas.CommentStats)
def get_comment_stats(db: Session = Depends(get_db)):
    # Total de comentarios
    total_comments = db.query(models.Comment).count()
    
    # Comentarios aprobados
    approved_comments = db.query(models.Comment).filter(
        models.Comment.is_approved == True
    ).count()
    
    # Comentarios pendientes
    pending_comments = db.query(models.Comment).filter(
        models.Comment.is_approved == False
    ).count()
    
    # Comentarios por sección
    sections = db.query(
        models.Comment.page_section,
        func.count(models.Comment.id).label('count')
    ).group_by(models.Comment.page_section).all()
    
    section_stats = {section: count for section, count in sections}
    
    return {
        "success": True,
        "total_comments": total_comments,
        "approved_comments": approved_comments,
        "pending_comments": pending_comments,
        "sections": section_stats
    }

# POST - Aprobar/desaprobar comentario
@router.post("/{comment_id}/approve")
def toggle_comment_approval(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    
    db_comment.is_approved = not db_comment.is_approved
    db.commit()
    
    status = "aprobado" if db_comment.is_approved else "pendiente"
    
    return {
        "success": True,
        "message": f"Comentario marcado como {status}",
        "is_approved": db_comment.is_approved
    }

# GET - Respuestas de un comentario
@router.get("/{comment_id}/replies", response_model=schemas.CommentList)
def get_comment_replies(comment_id: int, db: Session = Depends(get_db)):
    # Verificar que el comentario padre existe
    parent_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not parent_comment:
        raise HTTPException(status_code=404, detail="Comentario padre no encontrado")
    
    replies = db.query(models.Comment).filter(
        models.Comment.parent_id == comment_id,
        models.Comment.is_approved == True
    ).order_by(models.Comment.created_at).all()
    
    return {
        "success": True,
        "count": len(replies),
        "total_count": len(replies),
        "data": replies
    }
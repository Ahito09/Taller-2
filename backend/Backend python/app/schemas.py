from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from datetime import datetime

# Esquema base para comentarios
class CommentBase(BaseModel):
    user_name: str
    user_email: EmailStr
    content: str
    page_section: str
    post_id: Optional[int] = None
    rating: Optional[int] = None
    parent_id: Optional[int] = None

    @validator('user_name')
    def validate_user_name(cls, v):
        if len(v.strip()) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        return v.strip()

    @validator('content')
    def validate_content(cls, v):
        if len(v.strip()) < 5:
            raise ValueError('El comentario debe tener al menos 5 caracteres')
        if len(v) > 1000:
            raise ValueError('El comentario no puede exceder 1000 caracteres')
        return v.strip()

    @validator('rating')
    def validate_rating(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError('El rating debe estar entre 1 y 5')
        return v

    @validator('page_section')
    def validate_page_section(cls, v):
        allowed_sections = ['home', 'about', 'blog', 'contact', 'services', 'products']
        if v not in allowed_sections:
            raise ValueError(f'Sección no válida. Permitidas: {", ".join(allowed_sections)}')
        return v

# Esquema para crear comentario
class CommentCreate(CommentBase):
    pass

# Esquema para actualizar comentario
class CommentUpdate(BaseModel):
    content: Optional[str] = None
    rating: Optional[int] = None
    is_approved: Optional[bool] = None

    @validator('content')
    def validate_content(cls, v):
        if v is not None:
            if len(v.strip()) < 5:
                raise ValueError('El comentario debe tener al menos 5 caracteres')
            if len(v) > 1000:
                raise ValueError('El comentario no puede exceder 1000 caracteres')
        return v.strip() if v else v

# Esquema para respuesta de comentario
class CommentResponse(CommentBase):
    id: int
    is_approved: bool
    is_edited: bool
    edited_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    reply_count: int = 0

    class Config:
        from_attributes = True

# Esquema para comentario con respuestas
class CommentWithReplies(CommentResponse):
    replies: List['CommentResponse'] = []

# Esquema para listado
class CommentList(BaseModel):
    success: bool
    count: int
    total_count: int
    data: List[CommentResponse]

# Esquema para estadísticas
class CommentStats(BaseModel):
    success: bool
    total_comments: int
    approved_comments: int
    pending_comments: int
    sections: dict

# Esquema para respuesta de operación
class OperationResponse(BaseModel):
    success: bool
    message: str
    comment_id: Optional[int] = None
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False, index=True)  # ← String sin argumentos
    user_email = Column(String, nullable=False, index=True)  # ← String sin argumentos
    content = Column(Text, nullable=False)
    page_section = Column(String, nullable=False)  # ← String sin argumentos
    post_id = Column(Integer, nullable=True)
    rating = Column(Integer, default=0)
    is_approved = Column(Boolean, default=False)
    is_edited = Column(Boolean, default=False)
    edited_at = Column(DateTime, nullable=True)
    parent_id = Column(Integer, ForeignKey('comments.id'), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relación para respuestas
    replies = relationship("Comment", back_populates="parent", remote_side=[id])
    parent = relationship("Comment", back_populates="replies", remote_side=[parent_id])

    def __repr__(self):
        return f"<Comment by {self.user_name} on {self.page_section}>"
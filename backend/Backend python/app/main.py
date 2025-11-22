from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, get_db
from app import models
from app.routes import comments
import os
from dotenv import load_dotenv

load_dotenv()

# Crear tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Comments API",
    description="API para gestión de comentarios en la página con FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(comments.router)

@app.get("/")
def read_root():
    return {
        "message": "💬 Comments API con FastAPI funcionando!",
        "database": "PostgreSQL",
        "docs": "/docs",
        "endpoints": {
            "comments": "/api/comments",
            "stats": "/api/comments/stats/summary",
            "by_section": "/api/comments/section/{section}"
        }
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI Comments API",
        "database": "PostgreSQL"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 3002))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
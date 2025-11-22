import os
import sys

print("🔍 Verificando estructura de archivos...")

# Verificar archivos existentes
files_to_check = [
    "app/__init__.py",
    "app/main.py", 
    "app/database.py",
    "app/models.py",
    "app/schemas.py",
    "app/routes/__init__.py",
    "app/routes/comments.py",
    ".env"
]

for file in files_to_check:
    if os.path.exists(file):
        print(f"✅ {file} - EXISTE")
    else:
        print(f"❌ {file} - NO EXISTE")

print("\n🔍 Verificando imports...")
try:
    from app.database import engine, get_db
    print("✅ from app.database import engine, get_db - OK")
    
    from app import models
    print("✅ from app import models - OK")
    
    from app.routes import comments
    print("✅ from app.routes import comments - OK")
    
    print("\n🎉 ¡Todas las importaciones funcionan correctamente!")
    
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    
    # Mostrar contenido de database.py para debug
    if os.path.exists("app/database.py"):
        print("\n📄 Contenido de app/database.py:")
        with open("app/database.py", "r") as f:
            print(f.read())
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.core.config import settings
from app.routers.api import api_router
from app.db.session import engine 
from app.db.base_class import Base #
from app.db.init_db import init_db 
from app.db.session import SessionLocal 

# Crear tablas (solo si no existen). Para producción, usar Alembic.
# Base.metadata.create_all(bind=engine)
def try_init_db():
    db = SessionLocal()
    try:
        init_db(db)
        print("Base de datos inicializada/verificada.")
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")
    finally:
        db.close()

# Descomentar para ejecutar al inicio si no se usa Alembic
# try_init_db() # Mantener comentado si se usa el evento startup


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configuración de CORS
# Ajustar origins según sea necesario para producción
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"], # Origen del frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": f"Bienvenido a {settings.PROJECT_NAME}"}

# Si se usa uvicorn main:app --reload, esto puede ser útil para inicializar la BD una vez
@app.on_event("startup")
async def on_startup():
    print("Aplicación iniciada. Intentando inicializar DB...")
    try_init_db()

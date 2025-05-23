from sqlalchemy.orm import Session
from app.db.base_class import Base 
from app.db.session import engine
from app.models.article_model import SavedArticle 

def init_db(db: Session) -> None:
    # Crear tablas en la base de datos
    # Solo se crearán si no existen.
    Base.metadata.create_all(bind=engine)

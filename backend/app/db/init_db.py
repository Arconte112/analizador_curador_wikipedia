from sqlalchemy.orm import Session
from app.db.base_class import Base # Asegúrate que los modelos se importen aquí para que Base los conozca
from app.db.session import engine
# Importar todos los modelos aquí para que Base los registre:
from app.models.article_model import SavedArticle # Modelo de artículo guardado
# from app.models.article import Article # Ejemplo

def init_db(db: Session) -> None:
    # Crear tablas en la base de datos
    # Solo se crearán si no existen.
    Base.metadata.create_all(bind=engine)

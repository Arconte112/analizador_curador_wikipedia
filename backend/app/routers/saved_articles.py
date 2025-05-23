from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services import article_crud_service
from app.schemas.article_schema import SavedArticleInDB, SavedArticleCreate, SavedArticleUpdate

router = APIRouter()

@router.post("/", response_model=SavedArticleInDB, status_code=201)
def create_new_saved_article(
    article: SavedArticleCreate, 
    db: Session = Depends(get_db)
):
    """
    Guarda un nuevo artículo.
    """
    db_article_by_url = article_crud_service.get_saved_article_by_url(db, str(article.url_wikipedia))
    if db_article_by_url:
        raise HTTPException(status_code=400, detail="Este artículo ya está guardado (misma URL).")
    return article_crud_service.create_saved_article(db=db, article=article)

@router.get("/", response_model=List[SavedArticleInDB])
def read_saved_articles(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    Obtiene una lista de artículos guardados.
    """
    articles = article_crud_service.get_saved_articles(db, skip=skip, limit=limit)
    return articles

@router.get("/{article_id}", response_model=SavedArticleInDB)
def read_single_saved_article(
    article_id: int, 
    db: Session = Depends(get_db)
):
    """
    Obtiene un artículo guardado específico por su ID.
    """
    db_article = article_crud_service.get_saved_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artículo guardado no encontrado.")
    return db_article

@router.put("/{article_id}", response_model=SavedArticleInDB)
def update_existing_saved_article(
    article_id: int,
    article_in: SavedArticleUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza un artículo guardado. (Uso limitado en este proyecto, más para notas)
    """
    db_article = article_crud_service.get_saved_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artículo guardado no encontrado.")
    return article_crud_service.update_saved_article(db=db, db_article=db_article, article_in=article_in)

@router.delete("/{article_id}", response_model=SavedArticleInDB)
def delete_existing_saved_article(
    article_id: int, 
    db: Session = Depends(get_db)
):
    """
    Elimina un artículo guardado.
    """
    db_article = article_crud_service.delete_saved_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artículo guardado no encontrado.")
    return db_article 

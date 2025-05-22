from sqlalchemy.orm import Session
from app.models.article_model import SavedArticle
from app.schemas.article_schema import SavedArticleCreate, SavedArticleUpdate
from typing import List, Optional

def get_saved_article(db: Session, article_id: int) -> Optional[SavedArticle]:
    return db.query(SavedArticle).filter(SavedArticle.id == article_id).first()

def get_saved_article_by_url(db: Session, url: str) -> Optional[SavedArticle]:
    return db.query(SavedArticle).filter(SavedArticle.url_wikipedia == url).first()

def get_saved_articles(db: Session, skip: int = 0, limit: int = 100) -> List[SavedArticle]:
    return db.query(SavedArticle).offset(skip).limit(limit).all()

def create_saved_article(db: Session, article: SavedArticleCreate) -> SavedArticle:
    db_article = SavedArticle(
        title_wikipedia=article.title_wikipedia,
        url_wikipedia=str(article.url_wikipedia), # Asegurar que es string
        summary_processed=article.summary_processed,
        frequent_words=article.frequent_words,
        word_count=article.word_count
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_saved_article(db: Session, db_article: SavedArticle, article_in: SavedArticleUpdate) -> SavedArticle:
    update_data = article_in.model_dump(exclude_unset=True) # Pydantic V2
    # update_data = article_in.dict(exclude_unset=True) # Pydantic V1
    for key, value in update_data.items():
        setattr(db_article, key, value)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
    
def delete_saved_article(db: Session, article_id: int) -> Optional[SavedArticle]:
    db_article = db.query(SavedArticle).filter(SavedArticle.id == article_id).first()
    if db_article:
        db.delete(db_article)
        db.commit()
    return db_article

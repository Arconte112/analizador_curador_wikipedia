from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict
from datetime import datetime

# Para búsqueda en Wikipedia
class WikipediaSearchSuggestion(BaseModel):
    title: str
    page_id: Optional[str] = None # O el identificador que use la API de Wikipedia

class WikipediaSearchResult(BaseModel):
    suggestions: List[WikipediaSearchSuggestion]

# Para detalles del artículo de Wikipedia
class ArticleAnalysis(BaseModel):
    word_count: int
    frequent_words: Dict[str, int] # ej. {"palabra1": 5, "palabra2": 3}

class ArticleDetail(BaseModel):
    title: str
    processed_summary: str
    analysis: ArticleAnalysis
    original_url: HttpUrl

# Para artículos guardados (CRUD)
class SavedArticleBase(BaseModel):
    title_wikipedia: str
    url_wikipedia: HttpUrl
    summary_processed: Optional[str] = None
    frequent_words: Optional[Dict[str, int]] = None
    word_count: Optional[int] = None

class SavedArticleCreate(SavedArticleBase):
    pass

class SavedArticleUpdate(SavedArticleBase): # Podría ser Partial<SavedArticleCreate>
    title_wikipedia: Optional[str] = None
    url_wikipedia: Optional[HttpUrl] = None

class SavedArticleInDB(SavedArticleBase):
    id: int
    saved_at: datetime

    class Config:
        from_attributes = True # Pydantic V2, o orm_mode = True para V1

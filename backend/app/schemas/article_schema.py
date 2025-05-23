from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict
from datetime import datetime


class WikipediaSearchSuggestion(BaseModel):
    title: str
    page_id: Optional[str] = None 

class WikipediaSearchResult(BaseModel):
    suggestions: List[WikipediaSearchSuggestion]


class ArticleAnalysis(BaseModel):
    word_count: int
    frequent_words: Dict[str, int]

class ArticleDetail(BaseModel):
    title: str
    processed_summary: str
    analysis: ArticleAnalysis
    original_url: HttpUrl


class SavedArticleBase(BaseModel):
    title_wikipedia: str
    url_wikipedia: HttpUrl
    summary_processed: Optional[str] = None
    frequent_words: Optional[Dict[str, int]] = None
    word_count: Optional[int] = None

class SavedArticleCreate(SavedArticleBase):
    pass

class SavedArticleUpdate(SavedArticleBase):
    title_wikipedia: Optional[str] = None
    url_wikipedia: Optional[HttpUrl] = None

class SavedArticleInDB(SavedArticleBase):
    id: int
    saved_at: datetime

    class Config:
        from_attributes = True

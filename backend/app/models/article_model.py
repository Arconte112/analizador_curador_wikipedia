from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from app.db.base_class import Base

class SavedArticle(Base):
    __tablename__ = "saved_articles" 

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title_wikipedia = Column(String, nullable=False, index=True)
    url_wikipedia = Column(String, nullable=False, unique=True, index=True)
    summary_processed = Column(Text, nullable=True)
    frequent_words = Column(JSON, nullable=True) 
    word_count = Column(Integer, nullable=True)
    saved_at = Column(DateTime(timezone=True), server_default=func.now())
 

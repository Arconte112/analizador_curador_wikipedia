from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.services import wikipedia_service, analysis_service
from app.schemas.article_schema import WikipediaSearchResult, ArticleDetail, WikipediaSearchSuggestion

router = APIRouter()

@router.get("/search", response_model=WikipediaSearchResult)
def search_articles_endpoint(
    term: str = Query(..., min_length=1, description="Término de búsqueda para Wikipedia")
):
    """
    Busca artículos en Wikipedia basados en un término.
    """
    suggestions_data = wikipedia_service.search_wikipedia_articles(term)
    if not suggestions_data:
       
        return WikipediaSearchResult(suggestions=[]) 
    
    suggestions = [WikipediaSearchSuggestion(title=s["title"]) for s in suggestions_data]
    return WikipediaSearchResult(suggestions=suggestions)

@router.get("/article-details", response_model=ArticleDetail)
def get_article_details_endpoint(
    title: str = Query(..., description="Título exacto del artículo de Wikipedia")
):
    """
    Obtiene detalles y análisis de un artículo específico de Wikipedia.
    """
    article_data = wikipedia_service.get_wikipedia_article_details(title)
    if not article_data:
        raise HTTPException(status_code=404, detail="Artículo de Wikipedia no encontrado.")

    analysis_results = analysis_service.analyze_text_content(article_data["full_text"])
    
    return ArticleDetail(
        title=article_data["title"],
        processed_summary=article_data["processed_summary"],
        analysis=analysis_results,
        original_url=article_data["original_url"]
    )

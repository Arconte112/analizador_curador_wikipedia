import wikipediaapi
import requests # Alternativa o para obtener contenido crudo si es necesario
from app.core.config import settings
from nltk.tokenize import sent_tokenize # Para resumen simple

# Configurar User-Agent para wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(
    language='es',  # O el idioma deseado
    user_agent=settings.WIKIPEDIA_USER_AGENT
)

def search_wikipedia_articles(term: str, limit: int = 5) -> list:
    """Busca artículos en Wikipedia."""
    try:
        # wikipedia-api no tiene una función de búsqueda directa de "sugerencias" como la web.
        # page_py = wiki_wiki.page(term) # Esto obtiene una página si el título es exacto
        # Para una búsqueda más general, se podría usar la API de MediaWiki directamente con requests
        # Ejemplo con requests para opensearch:
        api_url = "https://es.wikipedia.org/w/api.php"
        params = {
            "action": "opensearch",
            "search": term,
            "limit": str(limit),
            "namespace": "0", # Solo artículos
            "format": "json"
        }
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        # Formato de respuesta: [searchTerm, [titles], [descriptions], [urls]]
        search_results = response.json()
        if search_results and len(search_results) > 1:
            titles = search_results[1]
            # page_ids no vienen directamente con opensearch, se podrían obtener con otra llamada si es necesario
            return [{"title": title} for title in titles]
        return []
    except requests.RequestException as e:
        print(f"Error al buscar en Wikipedia: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado en search_wikipedia_articles: {e}")
        return []

def get_wikipedia_article_details(title: str) -> dict | None:
    """Obtiene el contenido y resumen de un artículo de Wikipedia."""
    try:
        page = wiki_wiki.page(title)
        if not page.exists():
            return None

        # Resumen simple (primeros N párrafos o frases)
        # El atributo .summary de wikipedia-api ya da un resumen.
        # Si se quiere más control, se puede tomar page.text y procesarlo.
        # summary_text = page.summary # Resumen por defecto de la librería
        
        # Para un resumen más controlado (ej. 3 primeras frases del contenido completo)
        # Esto puede ser muy largo, el .summary suele ser mejor.
        # sentences = sent_tokenize(page.text)
        # processed_summary = " ".join(sentences[:3]) if len(sentences) >=3 else page.summary

        processed_summary = page.summary # Usar el resumen de la librería por simplicidad inicial

        return {
            "title": page.title,
            "full_text": page.text, # Texto completo para análisis
            "processed_summary": processed_summary,
            "original_url": page.fullurl
        }
    except Exception as e:
        print(f"Error al obtener detalles del artículo '{title}': {e}")
        return None

from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

try:
    stop_words_es = set(stopwords.words('spanish'))
except LookupError:
    # Esto es un fallback si nltk.download no se ejecutó o falló
    print("NLTK stopwords for Spanish not found. Downloading...")
    import nltk
    nltk.download('stopwords', quiet=True)
    stop_words_es = set(stopwords.words('spanish'))

try:
    # Verificar si 'punkt' está disponible, necesario para word_tokenize
    word_tokenize("test", language='spanish')
except LookupError:
    print("NLTK punkt tokenizer models not found. Downloading 'punkt' and 'punkt_tab'...")
    import nltk
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True) # Ensure punkt_tab is also downloaded

# Añadir palabras comunes o irrelevantes si es necesario
additional_stopwords = {'ej', 'mas', 'ser', 'haber', 'puede', 'si', 'solo', 'tan'}
stop_words_es.update(additional_stopwords)

def analyze_text_content(text: str, top_n_words: int = 10) -> dict:
    """Realiza un análisis simple del texto: conteo de palabras y palabras más frecuentes."""
    if not text:
        return {"word_count": 0, "frequent_words": {}}

    # Normalizar texto: minúsculas y quitar puntuación básica
    text_lower = text.lower()
    text_cleaned = re.sub(r'[^\w\s]', '', text_lower) # Quita puntuación

    words = word_tokenize(text_cleaned, language='spanish')
    
    # Filtrar stop words y palabras de longitud 1 (a menudo ruido)
    filtered_words = [
        word for word in words 
        if word.isalpha() and word not in stop_words_es and len(word) > 1
    ]
    
    word_count_total = len(words) # O len(filtered_words) si se prefiere contar solo palabras significativas
    
    word_frequencies = Counter(filtered_words)
    most_common_words = dict(word_frequencies.most_common(top_n_words))
    
    return {
        "word_count": word_count_total, # O len(filtered_words)
        "frequent_words": most_common_words
    }

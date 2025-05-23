from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

try:
    stop_words_es = set(stopwords.words('spanish'))
except LookupError:
    print("NLTK stopwords for Spanish not found. Downloading...")
    import nltk
    nltk.download('stopwords', quiet=True)
    stop_words_es = set(stopwords.words('spanish'))

try:
    word_tokenize("test", language='spanish')
except LookupError:
    print("NLTK punkt tokenizer models not found. Downloading 'punkt' and 'punkt_tab'...")
    import nltk
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)

additional_stopwords = {'ej', 'mas', 'ser', 'haber', 'puede', 'si', 'solo', 'tan'}
stop_words_es.update(additional_stopwords)

def analyze_text_content(text: str, top_n_words: int = 10) -> dict:
    if not text:
        return {"word_count": 0, "frequent_words": {}}

    text_lower = text.lower()
    text_cleaned = re.sub(r'[^\w\s]', '', text_lower)

    words = word_tokenize(text_cleaned, language='spanish')
    
    filtered_words = [
        word for word in words 
        if word.isalpha() and word not in stop_words_es and len(word) > 1
    ]
    
    word_count_total = len(words)
    
    word_frequencies = Counter(filtered_words)
    most_common_words = dict(word_frequencies.most_common(top_n_words))
    
    return {
        "word_count": word_count_total,
        "frequent_words": most_common_words
    }

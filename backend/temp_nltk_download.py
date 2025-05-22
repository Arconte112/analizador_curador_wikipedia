import nltk
import sys

print("Attempting to download NLTK 'stopwords' and 'punkt' if not present...")

stopwords_downloaded_or_present = False
try:
    nltk.data.find('corpora/stopwords')
    print("NLTK 'stopwords' resource already present.")
    stopwords_downloaded_or_present = True
except nltk.downloader.DownloadError:
    print("NLTK 'stopwords' resource not found. Attempting download...")
    if nltk.download('stopwords', quiet=True): # Added quiet=True
        print("NLTK 'stopwords' downloaded successfully.")
        stopwords_downloaded_or_present = True
    else:
        print("Failed to download NLTK 'stopwords'.")
except Exception as e:
    print(f"An unexpected error occurred while checking/downloading 'stopwords': {e}")

punkt_downloaded_or_present = False
try:
    nltk.data.find('tokenizers/punkt')
    print("NLTK 'punkt' resource already present.")
    punkt_downloaded_or_present = True
except nltk.downloader.DownloadError:
    print("NLTK 'punkt' resource not found. Attempting download...")
    if nltk.download('punkt', quiet=True): # Added quiet=True
        print("NLTK 'punkt' downloaded successfully.")
        punkt_downloaded_or_present = True
    else:
        print("Failed to download NLTK 'punkt'.")
except Exception as e:
    print(f"An unexpected error occurred while checking/downloading 'punkt': {e}")

if stopwords_downloaded_or_present and punkt_downloaded_or_present:
    print("NLTK resources 'stopwords' and 'punkt' are available.")
    sys.exit(0) # Success
else:
    print("One or more NLTK resources could not be made available. Please check logs.")
    sys.exit(1) # Failure

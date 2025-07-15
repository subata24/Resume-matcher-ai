import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ✅ Download required NLTK data files (for Streamlit Cloud compatibility)
nltk.download('punkt')
nltk.download('stopwords')

def extract_job_keywords(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Clean the text
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

    # Filter tokens
    keywords = [
        word for word in tokens
        if word not in stop_words and word not in punctuation and word.isalpha()
    ]

    return set(keywords)
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')


download_nltk_data()

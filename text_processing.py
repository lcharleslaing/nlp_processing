# The above code is a Python script that performs the following operations on an input text:

# 1. Import necessary libraries such as NLTK, Transformers, and regular expressions.
# 2. Load the GPT2 tokenizer from the Transformers library.
# 3. Define a `process_input` function that preprocesses the input text by performing the following steps:
#    a. Remove stopwords using the `remove_stopwords` function.
#    b. Remove special characters and punctuation using the `remove_special_characters` function.
#    c. Remove extra whitespace using the `remove_extra_whitespace` function.
#    d. Convert the text to lowercase.
# 4. Define a `count_tokens` function that calculates the number of tokens in the text using the GPT2 tokenizer.

# The purpose of this script is to clean and optimize the text before sending it to an API, which helps conserve tokens.

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')


def process_input(input_text):
    filtered_text = remove_stopwords(input_text)
    cleaned_text = remove_special_characters(filtered_text)
    cleaned_text = remove_extra_whitespace(cleaned_text)
    cleaned_text = cleaned_text.lower()
    return cleaned_text


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = ' '.join(
        word for word in word_tokens if word.lower() not in stop_words)
    return filtered_text


def remove_special_characters(text):
    cleaned_text = re.sub(r'[^\w\s]', ' ', text)
    return cleaned_text


def remove_extra_whitespace(text):
    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    return cleaned_text


def count_tokens(text):
    return len(tokenizer.encode(text))

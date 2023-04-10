import os
import nltk
import pyperclip
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from transformers import GPT2Tokenizer
import tkinter as tk
from tkinter import scrolledtext

nltk.download('punkt')
nltk.download('stopwords')

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


def process_input(input_text):
    filtered_text = remove_stopwords(input_text)
    return filtered_text


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)

    filtered_text = ' '.join(
        word for word in word_tokens if word.lower() not in stop_words)
    return filtered_text


def count_tokens(text):
    return len(tokenizer.encode(text))


input_text = input("Enter text to process: ")

# Process the input text
processed_text = process_input(input_text)

# Calculate token usage
tokens_before = count_tokens(input_text)
tokens_after = count_tokens(processed_text)

# Copy processed input to clipboard
pyperclip.copy(processed_text)

# Calculate the percentage of tokens saved
tokens_saved_percentage = (
    (tokens_before - tokens_after) / tokens_before) * 100

print(f"Processed input: {processed_text}\nTokens used: {tokens_after}")
print(f"\nOriginal Text Tokens used: {tokens_before}")
print(
    f"\nTokens Saved: {tokens_before - tokens_after} ({tokens_saved_percentage:.2f}%)")

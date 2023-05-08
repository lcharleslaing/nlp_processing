# GPT Token Saver

This app is a text processor designed to work with GPT models (e.g., GPT-4). It does not work with GPT-3.5-Turbo as it doesn't understand the processed text the same.  It helps users save tokens while using GPT models by processing the input text. The app provides a GUI with an input box for pasting the original text, a dropdown menu for selecting the GPT model, and a button to process the text. After processing, it displays the processed text, the number of tokens used in the original and processed text, the percentage of tokens saved, and the cost based on the selected GPT model. The app also offers the option to copy the processed text to the clipboard, clear the input, and exit the application.  There is also a button if you want to preprocess a complete file and save it as a .txt file.  You choose the file and the location to be saved.

The application is built using Python and Tkinter for the user interface.

## Features

- Remove stopwords from the input text
- Calculate the number of tokens before and after processing
- Calculate the cost savings based on a fixed token price
- Copy the processed text to the clipboard
- Clear input field
- Exit the application

## Dependencies

- Python 3.7+
- Tkinter
- ttkthemes
- nltk
- transformers
- pyperclip

## Installation

1. Clone the repository or download the source code.

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the `nltk_setup.py` script to download the necessary NLTK data:

```bash
python nltk_setup.py
```

4. Run the `main_application.py` script to launch the application:

```bash
python main_application.py
```

## Usage

1. Paste your input text into the "Paste text" field.
2. Click the "Process Text" button to process the text and display the results.
3. Review the processed text, token information, and cost savings.
4. Click the "Copy Processed Text" button to copy the result to your clipboard.
5. Use the "Clear" button to clear the input field for a new text input.
6. Click the "Exit" button to close the application.

## License

This project is licensed under the MIT License.

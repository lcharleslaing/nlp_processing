import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import scrolledtext
from tkinter.font import Font
from ttkthemes import ThemedTk
import tooltip as ttp
import pyperclip
from dotenv import load_dotenv
import os
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkinter import StringVar
from tkinter import scrolledtext
from tkinter.font import Font
from ttkthemes import ThemedTk
from text_processing import process_input, count_tokens
# Add the choose_and_process_file function here


def choose_and_process_file():
    # Changed filetypes to accept all files
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                input_text = file.read()
            processed_text = process_input(input_text)
            save_processed_text(processed_text, file_path)
        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while processing the file: {e}")
    else:
        messagebox.showinfo("Info", "No file selected")


def save_processed_text(text, original_file_path):
    save_directory = filedialog.askdirectory()
    if save_directory:
        original_filename = os.path.basename(original_file_path)
        file_extension = os.path.splitext(original_filename)[
            1]  # Get the file extension
        save_filename = os.path.splitext(original_filename)[0]
        # Use the same file extension as the original file
        save_path = os.path.join(
            save_directory, f"{save_filename}_processed{file_extension}")
        try:
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"{original_filename}\n\n{text}")
            messagebox.showinfo("Info", "Processed text saved successfully")
        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while saving the file: {e}")
    else:
        messagebox.showinfo("Info", "Saving cancelled")


def save_processed_text(text, original_file_path):
    save_directory = filedialog.askdirectory()
    if save_directory:
        original_filename = os.path.basename(original_file_path)
        save_filename = os.path.splitext(original_filename)[0]
        save_path = os.path.join(
            save_directory, f"{save_filename}_processed.txt")
        try:
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"{original_filename}\n\n{text}")
            messagebox.showinfo("Info", "Processed text saved successfully")
        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while saving the file: {e}")
    else:
        messagebox.showinfo("Info", "Saving cancelled")


# The rest of the main_application.py script follows

load_dotenv()

gpt_3_5_turbo_price = float(os.getenv("GPT_3_5_TURBO_PRICE"))


def get_selected_model_price():
    selected_model = model_var.get()
    if selected_model == "GPT-3.5-turbo":
        return gpt_3_5_turbo_price
    # Add more conditions for other models and their respective prices
    # ...


def process_and_display():
    input_text = input_box.get("1.0", tk.END).strip()
    processed_text = process_input(input_text)
    tokens_before = count_tokens(input_text)
    tokens_after = count_tokens(processed_text)
    tokens_saved_percentage = (
        (tokens_before - tokens_after) / tokens_before) * 100
    result = f"Processed input: {processed_text}"
    token_info = f"Tokens used: {tokens_after}\n\nOriginal Text Tokens used: {tokens_before}"
    token_info += f"\n\nTokens Saved: {tokens_before - tokens_after} ({tokens_saved_percentage:.2f}%)"

    # Calculate cost using the price of the selected model
    cost_per_1k_tokens = get_selected_model_price()
    cost = (tokens_after / 1000) * cost_per_1k_tokens
    cost_text = f"Cost: ${cost:.5f}"
    token_info += f"\n\n{cost_text}"

    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)
    result_box.config(state=tk.DISABLED)

    token_info_box.config(state=tk.NORMAL)
    token_info_box.delete("1.0", tk.END)
    token_info_box.insert(tk.END, token_info)
    token_info_box.config(state=tk.DISABLED)


def copy_result():
    result_text = result_box.get(
        "1.0", tk.END).strip().replace("Processed input: ", "")
    pyperclip.copy(result_text)


# Create main window
root = ThemedTk(theme="arc")
root.title("Text Processor")
root.geometry("800x600")
root.attributes('-fullscreen', True)

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create separate frame for title label
title_frame = ttk.Frame(mainframe)
title_frame.grid(column=0, row=0, columnspan=4, sticky=(tk.W, tk.E))
title_font = Font(size=20, weight='bold')
title_label = ttk.Label(title_frame, text="GPT Token Saver", font=title_font)


# Add the new button for choosing and processing a file
choose_file_button = ttk.Button(
    mainframe, text="Choose and Process File", command=choose_and_process_file)
choose_file_button.grid(column=2, row=8, padx=10, pady=10, sticky=tk.E)

# Use pack method to center the title_label within the title_frame
title_label.pack(padx=10, pady=10, expand=True, anchor=tk.CENTER)

input_label = ttk.Label(mainframe, text="Paste text:")
input_label.grid(column=0, row=1, sticky=(tk.W), padx=10, pady=10)

input_box = scrolledtext.ScrolledText(mainframe, wrap=tk.WORD, height=15)
input_box.grid(column=0, row=2, columnspan=3,
               padx=10, pady=10, sticky=(tk.W, tk.E))

mainframe.columnconfigure(0, weight=1)

process_button = ttk.Button(
    mainframe, text="Process Text", command=process_and_display)
process_button.grid(column=0, row=3, padx=10, pady=10, sticky=(tk.W))

# Dropdown menu for selecting the model
model_var = StringVar()
model_var.set("GPT-3.5-turbo")  # Set the default model

models = ["GPT-3.5-turbo"]
# models = ["GPT-3.5-turbo", "GPT-4 - 8K context", "GPT-4 - 32K context"]

model_dropdown = ttk.OptionMenu(mainframe, model_var, *models)
model_dropdown.grid(column=2, row=3, padx=10, pady=10, sticky=(tk.W))

result_label = ttk.Label(mainframe, text="Processed Text:")
result_label.grid(column=0, row=4, sticky=(tk.W), padx=10, pady=10)

result_box = scrolledtext.ScrolledText(
    mainframe, wrap=tk.WORD, state=tk.DISABLED, height=15)
result_box.grid(column=0, row=5, columnspan=3,
                padx=10, pady=10, sticky=(tk.W, tk.E))

token_info_label = ttk.Label(mainframe, text="Token Information:")
token_info_label.grid(column=0, row=6, sticky=(tk.W), padx=10, pady=10)

token_info_box = scrolledtext.ScrolledText(
    mainframe, wrap=tk.WORD, state=tk.DISABLED, height=15)
token_info_box.grid(column=0, row=7, columnspan=3,
                    padx=10, pady=10, sticky=(tk.W, tk.E))

copy_button = ttk.Button(
    mainframe, text="Copy Processed Text", command=copy_result)
copy_button.grid(column=0, row=8, padx=10, pady=10, sticky=(tk.W))

exit_button = ttk.Button(mainframe, text="Exit", command=root.quit)
exit_button.grid(column=1, row=8, padx=10, pady=10, sticky=(tk.E))

# Add Clear Inputs button
clear_inputs_button = ttk.Button(
    mainframe, text="Clear", command=lambda: input_box.delete("1.0", tk.END))
clear_inputs_button.grid(column=1, row=3, padx=10, pady=10, sticky=(tk.W))

# Tooltips
ttp.createToolTip(process_button, "Click to process input text.")
ttp.createToolTip(copy_button, "Click to copy processed text.")
ttp.createToolTip(exit_button, "Click to exit the application.")

root.mainloop()

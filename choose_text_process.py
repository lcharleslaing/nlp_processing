import os
import tkinter as tk
from tkinter import filedialog, messagebox
from text_processing import process_input


def choose_and_process_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("All files", "*.*"), ("Text files", "*.txt")])

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
        save_filename = os.path.splitext(original_filename)[0]
        save_path = os.path.join(save_directory, f"{save_filename}.txt")

        try:
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"{original_filename}: {text}")

            messagebox.showinfo("Info", "Processed text saved successfully")
        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while saving the file: {e}")
    else:
        messagebox.showinfo("Info", "Saving cancelled")


root = tk.Tk()
root.withdraw()

choose_and_process_file()

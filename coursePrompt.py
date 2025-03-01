import tkinter as tk
from tkinter import filedialog, messagebox
import re

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def extract_sentences():
    input_file = input_entry.get()
    output_file = output_entry.get()
    keyword = keyword_entry.get().strip()
    
    if not input_file or not output_file or not keyword:
        messagebox.showerror("Error", "Please select input/output files and enter a keyword.")
        return
    
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()
        
        sentences = re.split(r'(?<=[.!?])\s+', text)
        matching_sentences = [s for s in sentences if keyword.lower() in s.lower()]
        
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(matching_sentences))
        
        messagebox.showinfo("Success", f"Found {len(matching_sentences)} sentences. Saved to {output_file}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

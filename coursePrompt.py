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

# GUI setup
root = tk.Tk()
root.title("Sentence Extractor")

# Input file selection
tk.Label(root, text="Input File:").grid(row=0, column=0, padx=5, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Keyword entry
tk.Label(root, text="Keyword:").grid(row=1, column=0, padx=5, pady=5)
keyword_entry = tk.Entry(root, width=50)
keyword_entry.grid(row=1, column=1, padx=5, pady=5)

# Output file selection
tk.Label(root, text="Output File:").grid(row=2, column=0, padx=5, pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_output_file).grid(row=2, column=2, padx=5, pady=5)

# Extract button
tk.Button(root, text="Extract Sentences", command=extract_sentences).grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()

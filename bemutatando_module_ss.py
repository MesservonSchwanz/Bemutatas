# bemutatando_module_ss.py
import tkinter as tk
from tkinter import filedialog
import os  # Szükséges a fájl törléséhez

class FileHandlerSS:
    """Simple file handling class."""

    def __init__(self):
        self.filename = None

    def create_file_ss(self, filename):
        """Creates a new file."""
        try:
            with open(filename, 'w') as file:
                file.write("")
            return f"File created: {filename}"
        except Exception as e:
            return f"Error: {e}"

    def write_file_ss(self, filename, content):
        """Writes content to a file."""
        try:
            with open(filename, 'a') as file:
                file.write(content + "\n")
            return f"Content saved to: {filename}"
        except Exception as e:
            return f"Error: {e}"

    def read_file_ss(self, filename):
        """Reads content from a file."""
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found!"
        except Exception as e:
            return f"Error: {e}"

    def delete_file_ss(self, filename):
        """Deletes a file."""
        try:
            if os.path.exists(filename):
                os.remove(filename)
                return f"File deleted: {filename}"
            else:
                return "File not found!"
        except Exception as e:
            return f"Error: {e}"

def create_gui():
    """Creates a graphical user interface."""
    file_handler = FileHandlerSS()
    
    def create_file():
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename:
            result = file_handler.create_file_ss(filename)
            output_label.config(text=result)

    def write_file():
        filename = filedialog.askopenfilename()
        if filename:
            content = input_field.get("1.0", tk.END).strip()
            result = file_handler.write_file_ss(filename, content)
            output_label.config(text=result)

    def read_file():
        filename = filedialog.askopenfilename()
        if filename:
            result = file_handler.read_file_ss(filename)
            output_label.config(text=result)

    def delete_file():
        filename = filedialog.askopenfilename()
        if filename:
            result = file_handler.delete_file_ss(filename)
            output_label.config(text=result)
    
    root = tk.Tk()
    root.title("File Manager SS")
    root.geometry("400x400")

    tk.Button(root, text="Create New File", command=create_file).pack(pady=5)
    tk.Button(root, text="Write to File", command=write_file).pack(pady=5)
    tk.Button(root, text="Read File", command=read_file).pack(pady=5)
    tk.Button(root, text="Delete File", command=delete_file).pack(pady=5)  # New Delete File button

    global input_field
    input_field = tk.Text(root, height=5, width=40)
    input_field.pack(pady=5)

    global output_label
    output_label = tk.Label(root, text="")
    output_label.pack(pady=5)

    root.mainloop()
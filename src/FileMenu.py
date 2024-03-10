import tkinter as tk
import json
from striprtf.striprtf import rtf_to_text
from tkinter import filedialog
from utils.functions import get_lexemes, get_lexems_to_text


class FileMenu(tk.Frame):

    def __init__(self):
        self.filetypes = (
            ('RTF', '*.rtf'),
            ('TXT', '*.txt')
        )

    def open_file(self):
        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=self.filetypes
        )

        if filename:
            content = self.read_text_file(filename)

            new_window = tk.Toplevel()
            new_window.title(filename)
            new_window.geometry('400x300')
            text_widget = tk.Text(new_window)
            text_widget.insert('1.0', content)
            text_widget.pack()

    def parse_file(self):
        file_path = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=[('RTF', '*.rtf'), ('TXT', '*.txt')]
        )

        if file_path:
            content = self.read_text_file(file_path)
            lexems = get_lexemes(content)
            parsed_text = get_lexems_to_text(lexems)

            new_window = tk.Toplevel()
            new_window.title("Parsed File")
            new_window.geometry('500x400')
            text_widget = tk.Text(new_window)
            text_widget.insert('1.0', parsed_text)
            text_widget.pack()

    def parse_and_save_file(self):
        file_path = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=[('RTF', '*.rtf'), ('TXT', '*.txt')]
    )

        if file_path:
            content = self.read_text_file(file_path)
            lexems = get_lexemes(content)
            parsed_data = get_lexems_to_text(lexems)

            json_file_path = "data.json"

            with open(json_file_path, 'a') as json_file:
                for lexeme in parsed_data:
                    json_data = json.dumps(lexeme, ensure_ascii=False)
                    json_file.write(json_data + '\n')
        
            new_window = tk.Toplevel()
            new_window.title("Parsed File")
            new_window.geometry('500x400')
            text_widget = tk.Text(new_window)
            text_widget.insert('1.0', "Данные успешно сохранены в JSON-файл.")
            text_widget.pack()

    @staticmethod
    def read_text_file(file_path):
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        elif file_path.endswith('.rtf'):
            with open(file_path, 'r') as file: 
                rtf_text = file.read() 
                plain_text = rtf_to_text(rtf_text) 
                return plain_text
        else:
            print("Unsupported file format")
            return "Unsupported file format"
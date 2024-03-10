import tkinter as tk
from utils.file_utils import *
from src.HelpWindowMenu import HelpWindow
from src.WordGenerationMenu import WordGenerationMenu
from src.MainMenu import MainMenu
from src.FileMenu import FileMenu

class WordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Генератор словоформ")
        self.geometry("400x320")

        self.file_menu = FileMenu()

    def show_main_menu(self):
        self.clear_window()

        main_menu = MainMenu(self)
        main_menu.pack()

    def show_word_generation_menu(self):
        self.clear_window()

        word_generation_menu = WordGenerationMenu(self)
        word_generation_menu.pack()

    def show_help_window(self):
        help_window = HelpWindow(self)
        help_window.grab_set()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_normal_form_search(self):
        search_window = tk.Toplevel()
        search_window.title("Поиск по основе слова")

        normal_form_label = tk.Label(search_window, text="Основа слова:")
        normal_form_label.pack()
        self.normal_form = tk.Entry(search_window)
        self.normal_form.pack()

        search_button = tk.Button(search_window, text="Поиск", command=self.perform_normal_form_search)
        search_button.pack()

        self.search_result_label = tk.Label(search_window, text="")
        self.search_result_label.pack()

    def filter_by_part_of_speech(self):
        search_window = tk.Toplevel()
        search_window.title("Фильтрация по части речи")

        part_of_speech_label = tk.Label(search_window, text="Часть речи:")
        part_of_speech_label.pack()
        self.part_of_speech = tk.Entry(search_window)
        self.part_of_speech.pack()

        search_button = tk.Button(search_window, text="Поиск", command=self.perform_part_of_speech_search)
        search_button.pack()

        self.search_result_label = tk.Label(search_window, text="")
        self.search_result_label.pack()

    def filter_by_gender(self):
        search_window = tk.Toplevel()
        search_window.title("Фильтрация по роду")

        gender_label = tk.Label(search_window, text="Род:")
        gender_label.pack()
        self.gender = tk.Entry(search_window)
        self.gender.pack()

        search_button = tk.Button(search_window, text="Поиск", command=self.perform_gender_search)
        search_button.pack()

        self.search_result_label = tk.Label(search_window, text="")
        self.search_result_label.pack()

    def filter_by_case(self):
        search_window = tk.Toplevel()
        search_window.title("Фильтрация по падежу")

        case_label = tk.Label(search_window, text="Падеж:")
        case_label.pack()
        self.case = tk.Entry(search_window)
        self.case.pack()

        search_button = tk.Button(search_window, text="Поиск", command=self.perform_case_search)
        search_button.pack()

        self.search_result_label = tk.Label(search_window, text="")
        self.search_result_label.pack()

    def display_file_content(self):
        display_window = tk.Toplevel()
        display_window.title("Содержимое файла")

        text_box = tk.Text(display_window)
        text_box.insert(tk.END, view_data())
        text_box.pack()

        scrollbar = tk.Scrollbar(display_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=text_box.yview)
        text_box.config(yscrollcommand=scrollbar.set)

    def perform_part_of_speech_search(self):
        part_of_speech = self.part_of_speech.get()
        results = part_of_speech_filter(part_of_speech)

        self.show_result(results)

    def perform_normal_form_search(self):
        normal_form = self.normal_form.get()
        results = normal_form_search(normal_form)

        self.show_result(results)

    def perform_gender_search(self):
        gender = self.gender.get()
        results = gender_filter(gender)

        self.show_result(results)

    def perform_case_search(self):
        case = self.case.get()
        results = case_filter(case)

        self.show_result(results)

    def show_result(self, results):
        if results:
            result_text = "Найденные слова:\n"
            for result in results:
                result_text += f"{result}\n"
        else:
            result_text = "Слова не найдены."

        self.search_result_label.config(text=result_text)
import tkinter as tk
from tkinter import ttk
from utils.functions import generate_word_form
from utils.schemas import Word

class WordGenerationMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        base_label = tk.Label(self, text="Основа слова:")
        base_label.pack()
        self.base_entry = tk.Entry(self)
        self.base_entry.pack()

        gender_label = tk.Label(self, text="Род:")
        gender_label.pack()
        self.gender_combobox = ttk.Combobox(self, values=["мужской", "женский", "средний"], state="readonly")
        self.gender_combobox.pack()

        case_label = tk.Label(self, text="Падеж:")
        case_label.pack()
        self.case_combobox = ttk.Combobox(self, values=["именительный", "родительный", "дательный", "винительный",
                                                        "творительный", "предложный"], state="readonly")
        self.case_combobox.pack()

        number_label = tk.Label(self, text="Число:")
        number_label.pack()
        self.number_combobox = ttk.Combobox(self, values=["единственное", "множественное"], state="readonly")
        self.number_combobox.pack()

        generate_button = tk.Button(self, text="Сгенерировать слово", command=self.generate_word_helper)
        generate_button.pack()

        self.generated_word_label = tk.Label(self, text="")
        self.generated_word_label.pack()

        back_button = tk.Button(self, text="Назад", command=self.master.show_main_menu)
        back_button.pack()

    def generate_word_helper(self):
        base_word = self.base_entry.get()
        gender = self.gender_combobox.get()
        case = self.case_combobox.get()
        number = self.number_combobox.get()
        word = Word(normal_form=base_word, gender=gender, case=case, number=number)
        generated_word = generate_word_form(word)
        self.generated_word_label.config(text=f"Сгенерированное слово: {generated_word}")

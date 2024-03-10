import tkinter as tk

class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        generate_word_button = tk.Button(self, text='Генерация слова', command=master.show_word_generation_menu)
        generate_word_button.pack()

        open_button = tk.Button(self, text='Открыть файл txt или rtf', command=master.file_menu.open_file)
        open_button.pack()

        parsing_button = tk.Button(self, text='Разобрать файл txt или rtf', command=master.file_menu.parse_file)
        parsing_button.pack()

        parsing_and_save_button = tk.Button(self, text='Разобрать файл txt или rtf и сохранить', command=master.file_menu.parse_and_save_file)
        parsing_and_save_button.pack()

        search_by_normal_form = tk.Button(self, text='Поиск по основе слова', command=master.create_normal_form_search)
        search_by_normal_form.pack()

        part_of_speech_filter = tk.Button(self, text='Фильтрация по части речи', command=master.filter_by_part_of_speech)
        part_of_speech_filter.pack()

        gender_filter = tk.Button(self, text='Фильтрация по роду', command=master.filter_by_gender)
        gender_filter.pack()

        case_filter = tk.Button(self, text='Фильтрация по падежу', command=master.filter_by_case)
        case_filter.pack()

        view_data = tk.Button(self, text='Посмотреть файл с разбором', command=master.display_file_content)
        view_data.pack()

        help_button = tk.Button(self, text="Помощь", command=master.show_help_window)
        help_button.pack()
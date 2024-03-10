import tkinter as tk


class HelpWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Помощь")
        self.geometry("700x200")

        help_text = """
    Как пользоваться программой:
    1. Введите основу слова в поле "Основа слова".
    2. Выберите род слова из выпадающего списка "Род".
    3. Выберите падеж слова из выпадающего списка "Падеж".
    4. Выберите число слова из выпадающего списка "Число".
    5. Нажмите кнопку "Сгенерировать слово" для получения сгенерированной формы слова.
    6. Сгенерированное слово будет отображено внизу.
    """


        help_label = tk.Label(self, text=help_text, justify="left")
        help_label.pack()

        close_button = tk.Button(self, text="Закрыть", command=self.destroy)
        close_button.pack()
import tkinter as tk

from src.generator import SetGenerator
from src.utilities.constants import Constants
from tkinter import HORIZONTAL

class Gui:
    questions: list[str] = []
    max_questions_in_set: int

    def __init__(self, window) -> None:
        self.window = window
        self.set_generator = SetGenerator()
        self.window.minsize(800, 600)
        self.window['bg'] = '#2A2A2E'
        self.window.title('Set of questions generator')
        self.window.iconphoto(False, tk.PhotoImage(file='./images/icon.png'))

        self.label_nr_of_questions = tk.Label(
            self.window,
            text='Number of questions per set',
            bg=Constants.COLOUR_BACKGROUND,
            fg='white',
            font=(
                Constants.FONT_TYPEFACE,
                Constants.FONT_SIZE_REGULAR),
            pady=20)


        self.label_nr_of_sets = tk.Label(
            self.window,
            text='Number of sets',
            bg=Constants.COLOUR_BACKGROUND,
            fg='white',
            font=(
                Constants.FONT_TYPEFACE,
                Constants.FONT_SIZE_REGULAR),
            pady=20)

        self.slider_nr_of_sets = tk.Scale(self.window, from_=1, to=50, orient=HORIZONTAL)

        self.button_load_questions = tk.Button(
            self.window,
            text='Load Questions',

            background=Constants.COLOUR_BUTTON_BACKGROUND,
            bd=Constants.BUTTON_BORDER_SIZE,
            cursor=Constants.ACTIVE_CURSOR,
            command=lambda: self.handle_load_questions())

        self.button_generate_set = tk.Button(
            self.window,
            text='Generate Sets',
            background=Constants.COLOUR_BUTTON_BACKGROUND,
            bd=Constants.BUTTON_BORDER_SIZE,
            cursor=Constants.ACTIVE_CURSOR,
            command=lambda: self.handle_generate_sets())

        self.button_load_questions.grid(row=0, column=0)

    def handle_load_questions(self):
        self.questions = self.set_generator.load_questions_file()
        self.max_questions_in_set = len(self.questions)

        self.slider_nr_of_questions_per_set = tk.Scale(self.window, from_=1, to=self.max_questions_in_set, orient=HORIZONTAL)

        self.label_nr_of_questions.grid(row=1, column=0, sticky='nsew')
        self.slider_nr_of_questions_per_set.grid(row=1, column=1)
        self.label_nr_of_sets.grid(row=2, column=0, sticky='nsew')
        self.slider_nr_of_sets.grid(row=2, column=1)
        self.button_generate_set.grid(row=3, column=0)

    def handle_generate_sets(self):
        nr_of_sets = self.slider_nr_of_sets.get()
        nr_of_questions_per_set = self.slider_nr_of_questions_per_set.get()
        self.set_generator.generate_sets(self.questions, nr_of_sets, nr_of_questions_per_set)

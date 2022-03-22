import sys
import tkinter as tk
from src.generator import SetGenerator
from src.utilities.constants import Constants
from tkinter import HORIZONTAL
from os import path


class Gui:
    questions: list[str] = []
    max_questions_in_set: int

    x_coordinate = 60

    def __init__(self, window) -> None:
        self.window = window
        self.window.minsize(700, 400)
        self.window['bg'] = '#2A2A2E'
        self.window.title('Set of questions generator')

        if getattr(sys, 'frozen', False):
            application_path = path.dirname(sys.executable)
            path_to_icon = path.abspath(path.join(application_path, 'src/images/icon.png'))
        else:
            application_path = path.dirname(path.abspath(__file__))
            path_to_icon = path.abspath(path.join(application_path, 'images/icon.png'))

        self.window.iconphoto(False, tk.PhotoImage(file=path_to_icon))

        self.set_generator = SetGenerator()

        self.label_load_questions = self.create_label_descr('Load a text file containing a list of questions')
        self.button_load_questions = self.create_button('Load questions', lambda: self.handle_load_questions())
        self.label_msg_questions_loaded_successfully = self.create_label_msg('Questions loaded successfully')
        self.label_msg_file_location = None
        self.slider_nr_of_questions_per_set = None
        self.label_nr_of_questions_per_set = self.create_label_regular('Number of questions per set:')
        self.label_nr_of_sets = self.create_label_regular('Number of sets:')
        self.slider_nr_of_sets = self.create_scale(1, 50)
        self.button_generate_set = self.create_button('Generate new sets', lambda: self.handle_generate_sets())
        self.label_save_generated_sets_to_file = self.create_label_descr('Choose a location to save generated sets')
        self.button_save_generated_sets_to_file = self.create_button('Save sets',
                                                                     lambda: self.handle_save_generated_sets_to_file())
        self.label_msg_sets_generated_successfully = self.create_label_msg('Set of questions loaded successfully')
        self.label_msg_sets_saved_successfully = self.create_label_msg('Set of questions saved successfully')

        self.label_load_questions.place(x=self.x_coordinate, y=30)
        self.button_load_questions.place(x=self.x_coordinate + 5, y=65)

    def handle_load_questions(self):
        self.questions, filename = self.set_generator.load_questions_file()
        if not self.questions:  # user did not provide set of questions
            return

        self.label_msg_file_location = self.create_label_msg(f'File location: {filename}')
        self.label_msg_questions_loaded_successfully.after(2000,
                                                           self.label_msg_questions_loaded_successfully.place_forget)

        self.max_questions_in_set = len(self.questions)
        self.slider_nr_of_questions_per_set = self.create_scale(1, self.max_questions_in_set)

        self.label_msg_questions_loaded_successfully.place(x=self.x_coordinate, y=90)
        self.label_msg_file_location.place(x=self.x_coordinate, y=110)
        self.label_nr_of_questions_per_set.place(x=self.x_coordinate, y=140)
        self.slider_nr_of_questions_per_set.place(x=340, y=150)
        self.label_nr_of_sets.place(x=self.x_coordinate, y=190)
        self.slider_nr_of_sets.place(x=340, y=200)
        self.button_generate_set.place(x=self.x_coordinate+5, y=260)

    def handle_generate_sets(self):
        nr_of_sets = self.slider_nr_of_sets.get()
        nr_of_questions_per_set = self.slider_nr_of_questions_per_set.get()
        self.set_generator.generate_sets(self.questions, nr_of_sets, nr_of_questions_per_set)

        self.label_msg_sets_generated_successfully.place(x=self.x_coordinate, y=290)
        self.label_msg_sets_generated_successfully.after(2000,
                                                         self.label_msg_sets_generated_successfully.place_forget)
        self.button_save_generated_sets_to_file.place(x=self.x_coordinate+5, y=340)

    def handle_save_generated_sets_to_file(self):
        if not self.set_generator.save_generated_sets_to_file():
            return

        self.label_msg_sets_saved_successfully.place(x=self.x_coordinate, y=360)
        self.label_msg_sets_saved_successfully.after(2000,
                                                     self.label_msg_sets_saved_successfully.place_forget)

    def create_label_regular(self, label_text):
        return tk.Label(self.window,
                        text=label_text,
                        bg=Constants.COLOUR_BACKGROUND,
                        fg='white',
                        font=(
                            Constants.FONT_TYPEFACE,
                            Constants.FONT_SIZE_REGULAR),
                        pady=20)

    def create_label_msg(self, label_text):
        return tk.Label(self.window,
                        text=label_text,
                        bg=Constants.COLOUR_BACKGROUND,
                        fg='green',
                        font=(
                            Constants.FONT_TYPEFACE,
                            Constants.FONT_SIZE_MESSAGE))

    def create_label_descr(self, label_text):
        return tk.Label(self.window,
                        text=label_text,
                        bg=Constants.COLOUR_BACKGROUND,
                        fg=Constants.COLOUR_TEXT,
                        font=(
                            Constants.FONT_TYPEFACE,
                            Constants.FONT_SIZE_DESCRIPTION))

    def create_button(self, button_text, button_command):
        return tk.Button(self.window,
                         text=button_text,
                         background=Constants.COLOUR_BUTTON_BACKGROUND,
                         bd=Constants.BUTTON_BORDER_SIZE,
                         cursor=Constants.ACTIVE_CURSOR,
                         command=button_command)

    def create_scale(self, scale_from, scale_to):
        return tk.Scale(self.window,
                        from_=scale_from,
                        to=scale_to,
                        bg=Constants.COLOUR_BACKGROUND,
                        highlightbackground=Constants.COLOUR_BACKGROUND,
                        troughcolor='grey',
                        fg=Constants.COLOUR_TEXT,
                        bd=0,
                        orient=HORIZONTAL)

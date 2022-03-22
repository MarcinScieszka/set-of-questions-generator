import re
import random
from tkinter import filedialog


class SetGenerator:
    set_of_sets_of_questions: list[list[str]]
    questions: list[str] = []

    def load_questions_file(self) -> (list[str], str):
        """read questions from file and remove enumeration"""

        filename = filedialog.askopenfilename(title="Select a file containing a list of questions",
                                              filetypes=(('Text Document (*.txt)', '*.txt'), ('All Files', '.*')))
        if filename:
            with open(filename, 'r') as q:
                for question in q:
                    q1 = question.strip()
                    q2 = re.sub(r'^.*?\.', '', q1)  # remove numerations from questions
                    self.questions.append(q2.lstrip())

        return self.questions, filename

    def generate_sets(self, questions: list[str], nr_of_sets: int, nr_of_questions_per_set: int) -> None:
        """generate sets of questions from provided list of questions
           each set contains unique questions"""

        self.set_of_sets_of_questions = []
        current_set_of_questions: list[str] = []
        used_id_in_a_given_set: list[int] = []

        for i in range(1, nr_of_sets * nr_of_questions_per_set + 1):
            question_id: int = random.randint(0, len(questions) - 1)
            while question_id in used_id_in_a_given_set:
                # prevent duplicate questions in a given set
                question_id = random.randint(0, len(questions) - 1)

            used_id_in_a_given_set.append(question_id)
            current_set_of_questions.append(questions[question_id])

            if i % nr_of_questions_per_set == 0:
                self.set_of_sets_of_questions.append(current_set_of_questions)
                current_set_of_questions = []
                used_id_in_a_given_set = []

    def save_generated_sets_to_file(self) -> bool:
        """Save generated sets of questions into .txt file
           output location provided by user"""

        file_output = filedialog.askdirectory()
        if not file_output:
            return False

        with open(file_output + '/sets-of-questions.txt', 'w') as out:
            for num, given_set in enumerate(self.set_of_sets_of_questions):
                out.write(f'\nSet nr {num + 1}\n')
                for nr, question in enumerate(given_set):
                    out.write(f'{nr + 1}. {question}\n')
        return True

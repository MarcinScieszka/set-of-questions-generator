import re
import random
from tkinter import filedialog

class SetGenerator:

    @staticmethod
    def load_questions_file() -> list[str]:
        """read questions from file and remove enumeration"""

        questions: list[str] = []
        filename = filedialog.askopenfilename(title="Select a file containing a list of questions",
                                              filetypes=(('Text Document (*.txt)', '*.txt'), ('All Files', '.*')))
        with open(filename, 'r') as q:
            for question in q:
                q1 = question.strip()
                q2 = re.sub(r'^.*?\.', '', q1)  # remove numerations from questions
                questions.append(q2.lstrip())

        return questions

    def generate_sets(self, questions: list[str], nr_of_sets: int, nr_of_questions_per_set: int) -> None:
        set_of_sets_of_questions = []
        current_set_of_questions = []
        used_id_in_a_given_set = []

        file_output = filedialog.askdirectory()

        for i in range(1, nr_of_sets * nr_of_questions_per_set + 1):
            question_id = random.randint(0, len(questions) - 1)
            while question_id in used_id_in_a_given_set:
                # prevent duplicate questions in a given set
                question_id = random.randint(0, len(questions) - 1)

            used_id_in_a_given_set.append(question_id)
            current_set_of_questions.append(questions[question_id])

            if i % nr_of_questions_per_set == 0:
                set_of_sets_of_questions.append(current_set_of_questions)
                current_set_of_questions = []
                used_id_in_a_given_set = []

        with open(file_output + '/sets-of-questions.txt', 'w') as out:
            for num, given_set in enumerate(set_of_sets_of_questions):
                out.write(f'\nSet nr {num + 1}\n')
                for nr, question in enumerate(given_set):
                    out.write(f'{nr + 1}. {question}\n')

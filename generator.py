import re
import random
import tkinter as tk
from tkinter.filedialog import askopenfilename

def generate_demo_questions(num):
    """generate demo questions"""
    
    with open('demo-questions.txt', 'w') as f:
        for i in range(1, num+1):
            f.write(f'{i}. question nr {i}\n')

def get_questions():
    """read quesions from file and remove enumeration"""

    questions = []

    root = tk.Tk()
    root.withdraw()
    filename = askopenfilename(title="Please select a file containing a list of questions", 
                               filetypes=(('Text Document (*.txt)', '*.txt'), ('All Files', '.*')))
    
    with open(filename, 'r') as q:
        for question in q:
            q1 = question.strip()
            q2 = re.sub(r'^.*?\.', '', q1)
            questions.append(q2.lstrip())

    return questions

def main():
    # generate_demo_questions(5)
    questions = get_questions()

    # TODO: user defined numbers
    number_of_questions_in_set = 3
    number_of_sets = 20

    set_of_sets_of_questions = []
    current_set_of_questions = []
    used_id_in_a__given_set = []
    for i in range(1, number_of_sets*number_of_questions_in_set+1):
        quesion_id = random.randint(0, len(questions)-1)
        while quesion_id in used_id_in_a__given_set:
            # prevent duplicate questions in a given set
            quesion_id = random.randint(0, len(questions)-1)

        used_id_in_a__given_set.append(quesion_id)
        current_set_of_questions.append(questions[quesion_id])

        if i % number_of_questions_in_set == 0:
            set_of_sets_of_questions.append(current_set_of_questions)
            current_set_of_questions = []
            used_id_in_a__given_set = []
        
    with open('sets-of-questions.txt', 'w') as out:
        for num, set in enumerate(set_of_sets_of_questions):
            out.write(f'\nSet nr {num+1}\n')
            for nr, question in enumerate(set):
                out.write(f'{nr+1}. {question}\n')
            

if __name__ == "__main__":
    main()

import re
import random

def generate_demo_questions(num):
    """generate demo questions"""
    
    with open('demo-questions.txt', 'w') as f:
        for i in range(1, num+1):
            f.write(f'{i}. question nr {i}\n')

def get_questions():
    """read quesions from file and remove enumeration"""
    questions = []
    
    with open('demo-questions.txt', 'r') as q:
        for question in q:
            q1 = question.strip()
            q2 = re.sub(r'^.*?\. ', '', q1)
            questions.append(q2)

    return questions

def main():
    # generate_demo_questions(5)
    questions = get_questions()

    # TODO: user defined numbers
    number_of_questions_in_set = 3
    number_of_sets = 20

    set_of_sets_of_questions = []
    current_set_of_questions = []

    for i in range(1, number_of_sets*number_of_questions_in_set+1):
        quesion_id = random.randint(0, len(questions)-1)
        current_set_of_questions.append(questions[quesion_id])

        if i % number_of_questions_in_set == 0:
            set_of_sets_of_questions.append(current_set_of_questions)
            current_set_of_questions = []
    
    for num, set in enumerate(set_of_sets_of_questions):
        print(f'\nSet nr {num+1}')
        for question in set:
            print(f'{question}')
            

if __name__ == "__main__":
    main()

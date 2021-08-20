import re

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


if __name__ == "__main__":
    main()

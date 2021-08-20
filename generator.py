
def main():
   generate_demo_questions(5)

def generate_demo_questions(num):
    """generate demo questions"""
    
    with open('demo-questions.txt', 'w') as f:
        for i in range(1, num+1):
            f.write(f'{i}. question nr {i}\n')

if __name__ == "__main__":
    main()

import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operations = {'+': lambda number1, number2: number1 + number2,
                  '-': lambda number1, number2: number1 - number2,
                  '*': lambda number1, number2: number1 * number2}
    number1, number2 = random.randint(1, 50), random.randint(1, 50)
    operation = random.choice(list(operations.keys()))
    question = f'{number1} {operation} {number2}'
    correct_answer = str(operations[operation](number1, number2))
    return question, correct_answer

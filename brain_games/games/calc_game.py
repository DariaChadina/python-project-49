import random


DESCRIPTION = 'What is the result of the expression?'
game_rounds = 3


def generate_round():
    operations = {'+': lambda a, b: a + b,
                  '-': lambda a, b: a - b,
                  '*': lambda a, b: a * b}
    a, b = random.randint(1, 50), random.randint(1, 50)
    operation = random.choice(list(operations.keys()))
    question = f'{a} {operation} {b}'
    correct_answer = str(operations[operation](a, b))
    return question, correct_answer

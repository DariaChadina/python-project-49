from brain_games.game_logic import run_game, generate_question
import random


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    operations = {'+': lambda a, b: a + b,
                  '-': lambda a, b: a - b,
                  '*': lambda a, b: a * b}
    a, b = random.randint(1, 50), random.randint(1, 50)
    operation = random.choice(list(operations.keys()))
    question = f'{a} {operation} {b}'
    correct_answer = str(operations[operation](a, b))
    return generate_question(question, correct_answer)


def main():
    return run_game(3, DESCRIPTION, generate_round)

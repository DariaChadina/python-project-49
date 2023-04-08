from brain_games.game_logic import run_game, generate_question
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    question = random.randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return generate_question(question, correct_answer)


def main():
    return run_game(3, DESCRIPTION, generate_round)

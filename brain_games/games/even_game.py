from brain_games.game_logic import run_game, generate_question
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
game_rounds = 3


def generate_round():
    question = random.randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer

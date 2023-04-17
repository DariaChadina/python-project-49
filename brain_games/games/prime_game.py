from brain_games.game_logic import run_game, generate_question
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
game_rounds = 3


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer

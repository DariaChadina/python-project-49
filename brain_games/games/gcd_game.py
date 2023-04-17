from brain_games.game_logic import run_game, generate_question
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
game_rounds = 3


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer

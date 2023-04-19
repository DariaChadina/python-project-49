import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer

#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(num):
    return num % 2 == 0


def play_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_count = 0
    win_count = 3

    while correct_answers_count < win_count:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if (is_even(num) and answer == 'yes') or (not is_even(num) and answer == 'no'):
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if is_even(num) else 'no'}'.")
            print(f"Let's try again, {name}!")
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if play_game(name):
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

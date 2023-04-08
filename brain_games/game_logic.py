#!/usr/bin/env python3
import prompt


def run_game(game_rounds, game_description, generate_round):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_description)

    for _ in range(game_rounds):
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return False

    print(f'Congratulations, {name}!')
    return True


def generate_question(question, correct_answer):
    return (question, str(correct_answer))

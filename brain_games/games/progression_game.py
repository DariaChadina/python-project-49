from brain_games.game_logic import run_game, generate_question
import random
import prompt


DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    progression_length = random.randint(5, 10)
    start_num = random.randint(1, 50)
    step = random.randint(1, 5)
    hidden_index = random.randint(0, progression_length - 1)
    progression = [str(start_num + i * step) for i in range(progression_length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    return generate_question(question, correct_answer)


def main():
    return run_game(3, DESCRIPTION, generate_round)

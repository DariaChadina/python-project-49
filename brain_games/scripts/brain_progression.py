#!/usr/bin/env python3

from brain_games.game_logic import run_game
from brain_games.games import progression_game


def main():
    run_game(progression_game)
    return


if __name__ == '__main__':
    main()

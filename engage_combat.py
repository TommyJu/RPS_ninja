"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random

from get_choice_combat import get_choice_combat
from random_enemy_action import random_enemy_action
from does_player_win import does_player_win
from random import randint

def engage_combat(character, game_board, enemy_coordinates):
    print("an enemy approaches")
    victory = False
    while victory:
        print("You have:" + character["Current HP"] + "HP")
        player_action = (get_choice_combat(), random.randint(0, 10 + character["Attack Level"]))
        enemy_action = random_enemy_action()
        if does_player_win(player_action, enemy_action):
            victory = True
        else:
            character["Current HP"] -= ()




def main():
   pass


if __name__ == "__main__":
    main()

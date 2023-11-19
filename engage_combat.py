"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from get_choice_combat import get_choice_combat
from random_enemy_action import random_enemy_action

def engage_combat(character, game_board, enemy_coordinates):
    print("an enemy approaches")
    victory = False
    while victory:
        print("You have:" + character["Current HP"] + "HP")
        player_action = get_choice_combat()
        enemy_action = random_enemy_action()




def main():
    pass


if __name__ == "__main__":
    main()

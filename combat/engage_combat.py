"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random

from combat.get_choice_combat import get_choice_combat
from combat.random_enemy_action import random_enemy_action
from combat.does_player_win import does_player_win


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
            if (enemy_action[1] - player_action[1]) > 0:
                character["Current HP"] -= (enemy_action[1] - player_action[1])
            else:
                character["Current HP"] -= 1
    enemy_coordinates.remove([character["X-coordinate"], character["Y-coordinate"]])




def main():
   pass


if __name__ == "__main__":
    main()

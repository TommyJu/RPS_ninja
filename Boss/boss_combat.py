"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random

from is_boss_alive import is_boss_alive
from quick_time_event import quick_time_event
from choose_boss_attack_pattern import choose_boss_attack_pattern
from make_boss import make_boss
from character.is_alive import is_alive
from combat.does_player_win import does_player_win
from combat.get_choice_combat import get_choice_combat


def boss_combat(character, boss):
    while is_boss_alive(boss) and is_alive(character):
        print("You have:" + str(character["Current HP"]) + "HP")
        player_action = (get_choice_combat(), random.randint(0, 10) + character["Attack Level"])
        print("you used " + str(player_action[0]) + " with power " + str(player_action[1]))
        enemy_action = (choose_boss_attack_pattern(), random.randint(2, 12))
        print("enemy used " + str(enemy_action[0]) + " with power " + str(enemy_action[1]))
        if does_player_win(player_action, enemy_action):
            print("you won")
            return True
        else:
            if (enemy_action[1] - player_action[1]) > 0:
                character["Current HP"] -= (enemy_action[1] - player_action[1])
                print('you took ' + str(enemy_action[1] - player_action[1]) + ' dmg')
            else:
                character["Current HP"] -= 1
    return False



def main():
    pass


if __name__ == "__main__":
    main()

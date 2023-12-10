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
from character.is_alive import is_alive
from combat.does_player_win import does_player_win
from combat.get_choice_combat import get_choice_combat
from does_quick_time_occur import does_quick_time_occur
from resolve_quick_time import resolve_quick_time


def boss_combat(character: dict, boss: dict, attack_choice: str) -> bool:
    """
    Run boss combat

    determines if enemy widget needs to be removed
    Alter boss and character function by player actions and randomly chosen boss action

    :param character: dictionary representing player
    :param boss: dictionary representing hp
    :param attack_choice: string from the GUI input
    :precondition: Correctly determines if widget must be removed, If false remove the widget,
                   True if widget should be removed
                   Character must be a dictionary with key "Current HP" and "Attack Level" with values being integers
                   Boss must be a dictionary with key "Current HP"
                   attack_choice must be a string
    :postcondition: correctly determines if either boss of character dictionary is altered and by how much
                    Correctly determine if combat results in false, widget should be remove
                    or True, widget to be removed
    :return: Boolean representing the result of combat, True if enemy is defeated, False otherwise
    """
    if is_alive(boss) and is_alive(character):
        print("You have:" + str(character["Current HP"]) + "HP")
        if does_quick_time_occur():
            quick_time_input = quick_time_event()
            resolve_quick_time(quick_time_input, character)
            print(character)
        player_action = (get_choice_combat(attack_choice), random.randint(0, 10) + character["Attack Level"])
        print("you used " + str(player_action[0]) + " with power " + str(player_action[1]))
        enemy_action = (next(choose_boss_attack_pattern()), random.randint(2, 12))
        print("enemy used " + str(enemy_action[0]) + " with power " + str(enemy_action[1]))
        if does_player_win(player_action, enemy_action):
            if (player_action[1] - enemy_action[1]) > 0:
                boss["Current HP"] -= (player_action[1] - enemy_action[1])
                if is_alive(boss):
                    return True
                else:
                    return False
            else:
                boss["Current HP"] -= 1
                return False
        else:
            if (enemy_action[1] - player_action[1]) > 0:
                character["Current HP"] -= (enemy_action[1] - player_action[1])
                print('you took ' + str(enemy_action[1] - player_action[1]) + ' dmg')
                if does_quick_time_occur():
                    quick_time_input = quick_time_event()
                    resolve_quick_time(quick_time_input, character)
                    print(character)
            else:
                character["Current HP"] -= 1
    return False


def main():
    pass


if __name__ == "__main__":
    main()

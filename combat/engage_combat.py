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
from character.is_alive import is_alive


def engage_combat(character: dict, attack_choice: str):
    """
    run combat encounter

    player will be locked into combat until victory or player HP is 0. removes enemy engaged in combat in victory

    :param character: dictionary representing the users' character
    :param enemy_coordinates: list of lists representing coordinates of enemies
    :param enemy_widgets: a list of Tkinter labels for enemies
    :param vision_cones: list of lists or none representing coordinates of vision cones
    :param vision_cone_widgets: a list of Tkinter labels for enemy vision cones
    :param index: integer representing the index of the enemy engaged in combat
    :precondition: character is a dictionary with key "Current HP" with values being integer
                   character "Current HP" value is greater than 0 at beginning of engage combat
                   enemy_coordinates list of list representing the enemy current location
                   vision_cones list of lists representing the enemy detection or none if enemy is looking at location
                   not on board
                   index is integer associated with enemy currently engaged in combat
    :postcondition: remove enemy coordinate in combat and lantern associated with enemy in combat using the index
                    character value in key "Current HP" may change if player loses a round of RPS
    """
    if is_alive(character):
        print("You have:" + str(character["Current HP"]) + "HP")
        player_action = (get_choice_combat(attack_choice), (random.randint(0, 10) + character["Attack Level"]))
        print("you used " + str(player_action[0]) + " with power " + str(player_action[1]))
        enemy_action = random_enemy_action()
        print("enemy used " + str(enemy_action[0]) + " with power " + str(enemy_action[1]))
        print("\nAn enemy has spotted you! Choose your weapon to defeat the enemy:\n"
              "1. (R)ock\n"
              "2. (P)aper\n"
              "3. (S)cissors\n")
        if does_player_win(player_action, enemy_action):
            print("you won")
            return True
        else:
            if (enemy_action[1] - player_action[1]) > 0:
                character["Current HP"] -= (enemy_action[1] - player_action[1])
                print('you took ' + str(enemy_action[1] - player_action[1])+' dmg')
            else:
                character["Current HP"] -= 1
    return False


def main():
    pass


if __name__ == "__main__":
    main()

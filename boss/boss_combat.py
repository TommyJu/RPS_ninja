"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random
import time
# from quick_time_event import quick_time_event
# from choose_boss_attack_pattern import choose_boss_attack_pattern
from character.is_alive import is_alive
from combat.does_player_win import does_player_win
from combat.get_choice_combat import get_choice_combat
# from does_quick_time_occur import does_quick_time_occur
# from resolve_quick_time import resolve_quick_time


def resolve_quick_time(quick_time_result: tuple, character: dict):
    """
    change character dictionary value according to the results of the quick time event

    :param quick_time_result: tuple containg a Boolean value and a string
    :param character: dicitonary representing player character
    :precondition: quick_time_result must be a tuple where index 0 is a Boolean value and index 1 is a string
                   the string in quick time event must be one of "no damage", "minimal damage", "significant damage"
                   character must be a dictionary with key "Current HP" and "Attack Level" both with integer values
                   Character key-value "Current HP" must be greater than 0
    :postcondition: character dictionary values will change according to quick_time_result
                    if the boolean value in quick_time_event determines if "Current HP" will decrease
                    the string in quick_time_event will determine the change in "Attack Level"
    :return: dictionary that is changed according to results
    """
    if not quick_time_result[0]:
        match quick_time_result[1]:
            case "no damage":
                return character
            case "minimal damage":
                character["Attack Level"] -= 1
                return character
            case "significant damage":
                character["Attack Level"] -= 3
                return character
    else:
        if quick_time_result[1] == "counter":
            character["Current HP"] += 1
            character["Attack Level"] += 1
            return character
        return character

def determine_damage(player_time):
    """
    Determines the effect of player time

    :param player_time: floating point number representing how long it took for player to input
    :precondition: player_time must be a floating point number
                   function must be called in wrapper_timer
                   correctly determine which string to returen based on time value of player_time
    :return: string representing value of player_time
    """
    if player_time <= 1.0:
        return "counter"
    elif player_time <= 1.7:
        return "no damage"
    elif player_time <= 2.5:
        return "minimal damage"
    else:
        return "significant damage"

def timer(function):
    """
    measure input time and correctness

    :param function: function to be timed
    :return: tuple
    """

    def wrapper_timer(*args, **kwargs):
        input('entering quick time event\n press enter to start')
        start_time = time.perf_counter()
        quick_time_input = function(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        time_success = determine_damage(runtime)
        quick_time_result = (quick_time_input, time_success)
        print(quick_time_result)
        return quick_time_result

    return wrapper_timer



@timer
def quick_time_event():
    """
    Determine if user input is what the user was asked to type

    :precondition: quick time event was initiated
    :postcondition: correctly determines if user input is the equal to what was asked for
    :return: Boolean where True if correct input otherwise false
    """
    dodge = random.choice(['left', 'right', 'crouch', 'jump'])
    match dodge:
        case 'left':
            user_input = input('on you left!\n(type left)\n')
            return 'left' == user_input
        case 'right':
            user_input = input('on your right!\n(type right)\n')
            return 'right' == user_input
        case 'jump':
            user_inpt = input('watch out below!\n(type jump)\n')
            return 'jump' == user_inpt
        case 'crouch':
            user_input = input('watch out above!\n(type crouch)\n')
            return 'crouch' == user_input


def choose_boss_attack_pattern():
    choices = ["rock", "rock", "rock", "rock", "paper", "scissors"]
    yield random.choice(choices)


def does_quick_time_occur():
    """
    determine if a quick time event will occur randomly

    quick time event occurs with a 1 in 4 chance

    :precondition: player is engaged in boss combat
                   boss is alive
                   player is alive
    :postcondition: correctly determines the boolean value indicating if the event should occur
                    True if even occurs, False if event will not occur
    :return: boolean value
    """
    chance = random.randint(1, 4)
    return chance == 1

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
                   boss must be a dictionary with key "Current HP"
                   attack_choice must be a string
    :postcondition: correctly determines if either boss of character dictionary is altered and by how much
                    Correctly determine if combat results in false, widget should be remove
                    or True, widget to be removed
    :return: Boolean representing the result of combat, True if enemy is defeated, False otherwise
    """
    if is_alive(boss) and is_alive(character):
        print("\nYou have:" + str(character["Current HP"]) + "HP")
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

"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random
import time


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
        # input('entering quick time event\n press enter to start')
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
            # user_input = input('on you left!\n(type left)\n')
            print('on you left!\n(type left)\n')
            return 'left' == user_input
        case 'right':
            # user_input = input('on your right!\n(type right)\n')
            print('on your right!\n(type right)\n')
            return 'right' == user_input
        case 'jump':
            # user_input = input('watch out below!\n(type jump)\n')
            print('watch out below!\n(type jump)\n')
            return 'jump' == user_input
        case 'crouch':
            print('watch out above!\n(type crouch)\n')
            return 'crouch' == user_input


def main():
    pass


if __name__ == "__main__":
    main()

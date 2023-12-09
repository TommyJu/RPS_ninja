"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random
import time


def timer(function):
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




def determine_damage(player_time: float) -> str:
    """

    :param player_time:
    :return:
    """
    if player_time <= 1.0:
        return "counter"
    elif player_time <= 1.7:
        return "no damage"
    elif player_time <= 2.5:
        return "minimal damage"
    else:
        return "significant damage"


@timer
def quick_time_event():
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


def main():
    pass


if __name__ == "__main__":
    main()

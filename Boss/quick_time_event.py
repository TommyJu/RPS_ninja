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
        start_time = time.perf_counter()
        quick_time_input = function(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        time_success = runtime < 2.5
        return quick_time_input and time_success

    return wrapper_timer


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


print(quick_time_event())

def main():
    pass


if __name__ == "__main__":
    main()

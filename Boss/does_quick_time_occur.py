"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random


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



def main():
    pass


if __name__ == "__main__":
    main()

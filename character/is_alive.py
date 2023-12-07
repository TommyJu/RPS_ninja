"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def is_alive(character):
    """
    determine if character is still alive with hp > 0

    :param character: dictionary representing user character with key "Current HP" and an integer value
    :precondition: dictionary for character has key "Current HP"
                   "Current HP" key has value that is an integer
    :postcondition: correctly determines if character is still alive
    :return: Boolean value where True if character is alive and False if character is dead

    >>> is_alive({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5})
    True
    >>> is_alive({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0})
    False
    """
    return character["Current HP"] > 0


def main():
    pass


if __name__ == "__main__":
    main()
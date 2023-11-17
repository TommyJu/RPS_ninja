"""
Tommy Ju
A01347715

Matthew
A01373290
"""


def move_character(character, direction):
    """
    Update character coordinates based on user selected move direction

    :param character: a dictionary representing the game character
    :param direction: a string representing the move direction
    :precondition: character must be a dictionary created by the make_character function
    :precondition: direction must be either "north", "south", "east", or "west"
    :postcondition: updates the character dictionary coordinates one unit in the given direction
    """
    if direction == "north":
        character["Y-coordinate"] -= 1
    elif direction == "south":
        character["Y-coordinate"] += 1
    elif direction == "east":
        character["X-coordinate"] += 1
    else:
        character["X-coordinate"] -= 1


def main():
    pass


if __name__ == "__main__":
    main()

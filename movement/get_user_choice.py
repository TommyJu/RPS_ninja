"""
Tommy Ju
A01347715

Matthew
A01373290
"""
from movement.validate_move import validate_move


def get_user_choice(character, board, user_input):
    """
    Prompt the user to pick a direction

    :param board: dictionary representing play space
    :param character: dictionary representing the player
    :precondition: character must be a dictionary created by the make_character function
                   a valid direction must be given eventually
    :postcondition: retrieves the desired move direction from the user
    :return: a string representing move direction ("north", "south", "east", or "west")
    """
    acceptable_inputs = {"north", "south", "east", "west",
                         "w", "s", "d", "a",
                         "1", "2", "3", "4"}

    equivalent_inputs = [["north", "w", "1"],
                         ["south", "s", "2"],
                         ["east", "d", "3"],
                         ["west", "a", "4"]]

    print("Where do you wish to go? (Protip: type W, A, S, or D to move)\n"
          "1. North\n"
          "2. South\n"
          "3. East\n"
          "4. West\n")
    user_input = user_input.strip()
    # if user_input.lower() in acceptable_inputs:
    for direction in equivalent_inputs:
        if user_input.lower() in direction:
            # if validate_move(board, character, direction[0]):
            return direction[0]
#             else:
#                 print("move is not valid \n"
#                       "please keep movement on board")
# else:
#     print("\nPlease enter a valid direction.\n"
#           "To move north: type 'north', 'n', or '1'")


def main():
    pass


if __name__ == "__main__":
    main()

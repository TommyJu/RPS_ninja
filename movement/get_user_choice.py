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
                         "n", "s", "e", "w",
                         "1", "2", "3", "4"}

    equivalent_inputs = [["north", "n", "1"],
                         ["south", "s", "2"],
                         ["east", "e", "3"],
                         ["west", "w", "4"]]

    # while True:
    # user_input = input("Where do you wish to go?\n"
    #                    "1. (N)orth\n"
    #                    "2. (S)outh\n"
    #                    "3. (E)ast\n"
    #                    "4. (W)est\n")
    print("Where do you wish to go?\n"
          "1. (N)orth\n"
          "2. (S)outh\n"
          "3. (E)ast\n"
          "4. (W)est\n")
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

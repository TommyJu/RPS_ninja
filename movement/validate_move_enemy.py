"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def validate_move_enemy(enemy, board, enemies):
    """
    Give valid directions for an enemy's next move

    :param enemy: a list representing the coordinate of the current enemy being validated
    :param board: a dictionary representing the game board
    :param enemies: a list containing the lists for each enemy coordinate
    :precondition: board is a dictionary created by the make_board function
    :precondition: enemies is a list of valid coordinates created by the make_enemy function
    :postcondition: correctly gives an enemy's valid coordinates
    :return: a list containing lists of each valid enemy coordinate
    """
    possible_directions = [[enemy[0] - 1, enemy[1]], [enemy[0], enemy[1] + 1], [enemy[0] + 1, enemy[1]],
                          [enemy[0], enemy[1] - 1]]
    direction_choices = []
    for direction in possible_directions:
        direction_as_tuple = (direction[0], direction[1])
        if direction_as_tuple in board and [direction[0], direction[1]] not in enemies:
            direction_choices.append(direction)
    return direction_choices


def main():
    pass


if __name__ == "__main__":
    main()

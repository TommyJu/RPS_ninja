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
    end_point = list(max(board.keys()))
    start_point = [0, 0]
    # convert each coordinate tuple into a list
    board_coordinates = [list(coordinate) for coordinate in board]
    invalid_coordinates = enemies.copy()
    invalid_coordinates.append(start_point)
    invalid_coordinates.append(end_point)

    possible_directions = [[enemy[0] - 1, enemy[1]], [enemy[0], enemy[1] + 1], [enemy[0] + 1, enemy[1]],
                          [enemy[0], enemy[1] - 1]]
    direction_choices = []
    for direction in possible_directions:
        if direction in board_coordinates and direction not in invalid_coordinates:
            direction_choices.append(direction)
    return direction_choices


def main():
    pass


if __name__ == "__main__":
    main()

"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def validate_move_enemy(enemy, board, enemies):
    """

    :param enemy:
    :param board:
    :param enemies:
    :return:
    """
    possibe_directions = [[enemy[0] - 1, enemy[1]], [enemy[0], enemy[1] + 1], [enemy[0] + 1, enemy[1]],
                          [enemy[0], enemy[1] - 1]]
    direction_choices = []
    for direction in possibe_directions:
        direction_choices = []
        direction_as_set = (direction[0], direction[1])
        if direction_as_set in board and [direction[0], direction[1]] not in enemies:
            direction_choices.append(direction)
    return direction_choices


def main():
    pass


if __name__ == "__main__":
    main()

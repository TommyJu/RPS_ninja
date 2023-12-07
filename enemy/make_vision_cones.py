"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random


def make_vision_cones(enemy_coordinates, board):
    """
    Create vision for all enemies in a random valid direction

    A valid direction is not out of bounds, on an enemy, on the start point, or on the end point

    :param enemy_coordinates: a list of lists for each enemy coordinate
    :param board: a dictionary representing the game board
    :precondition: board must be a dictionary from the make_board function
    :postcondition: generate coordinates for enemy vision in a random and valid adjacent square

    :return: a list of lists for each enemy vision cone, a None value represents an enemy looking at an invalid square
    """
    vision_cones = []
    end_point = list(max(board.keys()))
    start_point = [0, 0]
    # convert each coordinate tuple into a list
    board_coordinates = [list(coordinate) for coordinate in board]
    invalid_coordinates = enemy_coordinates.copy()
    invalid_coordinates.append(start_point)
    invalid_coordinates.append(end_point)

    for enemy in enemy_coordinates:
        # Pick 1 of the 4 adjacent squares to an enemy at random
        direction = random.choice(["north", "east", "south", "west"])
        match direction:
            case "north":
                vision_cones.append([enemy[0], enemy[1] - 1])
            case "east":
                vision_cones.append([enemy[0] + 1, enemy[1]])
            case "south":
                vision_cones.append([enemy[0], enemy[1] + 1])
            case "west":
                vision_cones.append([enemy[0] - 1, enemy[1]])

        # If the vision cone we have just added is on an invalid square, assign to None.
        if vision_cones[-1] not in board_coordinates or vision_cones[-1] in invalid_coordinates:
            vision_cones[-1] = None

    return vision_cones

    # for enemy in enemy_coordinates:

    # return vision_cones


def main():
    pass


if __name__ == "__main__":
    main()

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

    :param enemy_coordinates: a list of lists for each enemy coordinate
    :param board: a dictionary representing the game board
    :precondition: board must be a dictionary from the make_board function
    :postcondition: generate coordinates for enemy vision in a random and valid adjacent square

    :return: a list of lists for each enemy vision cone, a None value represents an enemy looking out of bounds
    """
    vision_cones = []
    end_point = list(max(board.keys()))
    start_point = [0, 0]
    for enemy in enemy_coordinates:
        # Pick 1 of the 4 adjacent squares to an enemy at random
        random_adjacent_x = random.choice([-1, 1])
        random_adjacent_y = random.choice([-1, 1])

        vision_cones.append([enemy[0] + random_adjacent_x, enemy[1] + random_adjacent_y])

        # If the vision cone we have just added is on an invalid square, assign to None.
        if vision_cones[:-1] not in board or vision_cones[:-1] == start_point or vision_cones[:-1] == end_point:
            vision_cones[:-1] = None

    return vision_cones

    # for enemy in enemy_coordinates:
    #     direction = random.choice(["north", "east", "south", "west"])
    #     match direction:
    #         case"north":
    #             vision_cones.append([enemy[0], enemy[1] - 1])
    #         case "east":
    #             vision_cones.append([enemy[0] + 1, enemy[1]])
    #         case "south":
    #             vision_cones.append([enemy[0], enemy[1] + 1])
    #         case "west":
    #             vision_cones.append([enemy[0] - 1, enemy[1]])
    # return vision_cones


def main():
    pass


if __name__ == "__main__":
    main()

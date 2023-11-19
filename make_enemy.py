"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random


def make_enemy(game_board):
    """
    create a list of enemy locations

    :param game_board: dictionary made from make_board function representing play area
    :precondition: board is dictionary with keys being tuples representing location on board
    :postcondition: creates the correct amount of enemy randomly assigning a coordinate tuple
                    there are no duplicate coordinates in the array
                    no enemy will be created in starting coordinate

    :return: list of tuples representing enemy coordinates


    """

    list_of_coordinates = [coordinate for coordinate in game_board.keys()]
    # remove starting coordinate
    list_of_coordinates.remove((0, 0))
    enemy_count = 0
    enemy_coordinates = []
    while enemy_count < (len(game_board.keys()) // 2):
        random_coordinate = random.choice(list_of_coordinates)
        enemy_coordinates.append(random_coordinate)
        list_of_coordinates.remove(random_coordinate)
        enemy_count += 1

    return enemy_coordinates


def main():
    pass


if __name__ == "__main__":
    main()

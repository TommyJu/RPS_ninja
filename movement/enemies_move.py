"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random
from movement.validate_move_enemy import validate_move_enemy


def enemies_move(enemy_coordinates, visions, board):
    """
    Move enemy in a random direction and update enemy's range of vision

    :param enemy_coordinates: a list of representing enemy coordinates
    :param visions: a list representing vision cone coordinates
    :param board: a dictionary representing the game board
    :precondition: enemy_coordinates is a list of enemies created by the make_enemy function
    :precondition: visions is a list of vision cones created by the make_vision_cones function
    :precondition: board is a dictionary created by the make_board function
    :postcondition: move all enemies in a random direction, and then update the vision cone in that direction if valid
    """
    # Code for validating vision cone positions
    end_point = list(max(board.keys()))
    start_point = [0, 0]
    # convert each coordinate tuple into a list
    board_coordinates = [list(coordinate) for coordinate in board]
    invalid_coordinates = enemy_coordinates[:]
    invalid_coordinates.append(start_point)
    invalid_coordinates.append(end_point)

    # Move each enemy and their vision cone
    for enemy_index in range(len(enemy_coordinates)):
        # Move the enemy in a valid direction
        possible_directions = validate_move_enemy(enemy_coordinates[enemy_index], board, enemy_coordinates)
        if possible_directions:
            new_coordinate = random.choice(possible_directions)
            # determine the enemy movement direction by comparing with position before
            x_change = new_coordinate[0] - enemy_coordinates[enemy_index][0]
            y_change = new_coordinate[1] - enemy_coordinates[enemy_index][1]
            # Extend the vision cone using the new_coordinates and overwrite the existing if valid
            new_vision_cone_position = new_coordinate[0] + x_change, new_coordinate[1] + y_change
            # Update vision cone
            if new_vision_cone_position not in board_coordinates or new_vision_cone_position in invalid_coordinates:
                visions[enemy_index] = new_vision_cone_position
            else:
                visions[enemy_index] = None

            # Update the enemy position
            enemy_coordinates[enemy_index] = new_coordinate


def main():
    pass


if __name__ == "__main__":
    main()

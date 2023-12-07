"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random
from movement.validate_move_enemy import validate_move_enemy


def enemies_move(enemies, visions, board):
    """
    Move all enemies in a random direction

    :param enemies: a list of enemies created by the make_enemy function
    :param visions: a list of
    :param board:
    :return:
    """
    for enemy in enemies:
        index = enemies.index(enemy)
        possible_directions = validate_move_enemy(enemy, board, enemies)
        if possible_directions:
            new_coordinate = random.choice(possible_directions)
            x_change = new_coordinate[0] - enemy[0]
            y_change = new_coordinate[1] - enemy[1]
            old_vision = visions[index]
            new_vision = [old_vision[0]+x_change, old_vision[1]+y_change]
            visions[index] = new_vision
            enemies[index] = new_coordinate

def main():
    pass


if __name__ == "__main__":
    main()

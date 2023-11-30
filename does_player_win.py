"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random


def does_player_win(player_action, enemy_action):
    """

    :param player_action:
    :param enemy_action:
    :return:
    """
    choices = {'rock': 0, 'paper': 1, 'scissor': 2}
    result = choices[player_action] - choices[enemy_action[0]]
    winner = ['draw', 'you win', 'you lose']
    return winner[result]

def main():
    pass


if __name__ == "__main__":
    main()

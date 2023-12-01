"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def does_player_win(player_action, enemy_action):
    """

    :param player_action:
    :param enemy_action:
    :return:
    """
    choices = {'rock': 0, 'paper': 1, 'scissor': 2}
    result = choices[player_action[0]] - choices[enemy_action[0]]
    winner = ['draw', 'player win', 'player lose']
    match winner[result]:
        case 'draw':
            return player_action[1] >= enemy_action[1]
        case 'player win':
            return True
        case 'player lose':
            return False


def main():
    pass


if __name__ == "__main__":
    main()

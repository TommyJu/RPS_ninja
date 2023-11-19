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

    match player_action:
        case enemy_action[1]:
            return 'draw'
        case 'rock':
            match enemy_action[1]:
                case'paper':
                    return 'lose'
                case 'scissor':
                    return 'win'
        case 'paper':
            match enemy_action[1]:
                case 'scissor':
                    return 'lose'
                case 'rock':
                    return 'win'
        case 'scissor':
            match enemy_action[1]:
                case 'rock':
                    return 'lose'
                case 'paper':
                    return 'win'

def main():
    pass


if __name__ == "__main__":
    main()

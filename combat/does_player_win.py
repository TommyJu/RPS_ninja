"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def does_player_win(player_action, enemy_action):
    """
    Determines if player wins the combat encounter

    :param player_action: tuple representing the user input and random attack value
    :param enemy_action: tuple representing the randomly generated enemy action
    :precondition: player_action is a tuple with index 0 being a string in the results list
                   index 1 is an integer
                   enemy_action is a tuple with index 0 being a string in the results list
                   index 1 is an integer
    :postcondition: correctly determines if player wins the encounter, True if player win, False if player loses
    :return: Boolean representing player success in combat
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

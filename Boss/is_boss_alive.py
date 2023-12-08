"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
def is_boss_alive(boss):
    """
    determines if the boss is still alive
    :param boss: dictionary representing the boss
    :precondition: boss is a dictionary with key "Current HP"
    :postcondition: correctly determine if boss is alive
                    if boss is alive True, if boss dead False
    :return: Boolean value representing if boss is still alive
    """
    return boss["Current HP"] > 0

def main():
    pass


if __name__ == "__main__":
    main()

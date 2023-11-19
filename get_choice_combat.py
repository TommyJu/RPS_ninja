"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def get_choice_combat():
    """
    prompt user to choose how they want to attack

    :precondition: valid input is entered
    :postcondtion: retrieves the desired attack choice for valid input
                   print input prompt if valid input is not given
    :return: string representing rock, paper, or scissor
    """
    valid_input = ['1', '2', '3', 'rock', 'paper', 'scissor', 'r', 'p', 's']
    equivalent_inputs = [["rock", "r", "1"],
                         ["paper", "p", "2"],
                         ["scissor", "s", "3"]]
    while True:
        attack_input = input("Choose you weapon?\n"
                             "1. (R)ock\n"
                             "2. (P)aper\n"
                             "3. (S)cissor\n")
        attack_input = attack_input.strip()
        if attack_input.lower() in valid_input:
            for attack_choice in equivalent_inputs:
                if attack_input in attack_choice:
                    return attack_choice[0]
        else:
            print("\nPlease enter a valid attack choice.\n"
                  "EXAMPLE: To choose rock: type 'rock', 'r', or '1'")


def main():
    pass


if __name__ == "__main__":
    main()

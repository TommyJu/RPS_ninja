"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random
import itertools


# def choose_boss_attack_pattern():
#     rock_focus_pattern = []
#     scissor_focus_pattern = []
#     paper_focus_pattern = []
#     return random.choice([rock_focus_pattern, scissor_focus_pattern, paper_focus_pattern])
def choose_boss_attack_pattern():
    choices = ["rock", "rock", "rock", "rock", "paper", "scissors"]
    yield random.choice(choices)

def main():
    pass


if __name__ == "__main__":
    main()

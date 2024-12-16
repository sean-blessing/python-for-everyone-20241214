import random

def roll_die():
    return random.randint(1, 6)

def print_roll_summary(game_nbr, die1, die2):
    # print the roll summary:
    # - total
    # - special message:
    #   - snake eyes = two 1's
    #   - box cars = two 6's
    print(f'Game #[{game_nbr}] - Roll Summary:')
    total = die1 + die2
    print(f'Roll Total: {total}: [{die1}, {die2}]')
    if total == 2:
        print('Snake Eyes!')
    elif total == 12:
        print("Box Cars!")
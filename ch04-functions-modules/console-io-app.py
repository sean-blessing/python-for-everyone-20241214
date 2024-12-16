import die_roll_module

def main():
    print('Welcome to the Console IO App')
    number_games = int(input('How many games to play? '))

    for i in range(number_games):
        # roll a die (whole number between 1 and 6)
        die1 = die_roll_module.roll_die()
        # roll another die
        die2 = die_roll_module.roll_die()
        die_roll_module.print_roll_summary(i+1, die1, die2)

    print('Bye')


if __name__ == '__main__':
    main()
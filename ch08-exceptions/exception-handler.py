print('Welcome to the Exception Handler')

def get_int(prompt):
    nbr = 0
    while True:
        try:
            nbr = int(input(prompt))
            break
        except:
            print('Error: Invalid whole number.')
    return nbr

day = get_int('Day of Month: ')
month = get_int('Month: ')
year = get_int('Year: ')

print('Bye')
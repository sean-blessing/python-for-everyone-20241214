print('Welcome')

try:
    month = int(input('Enter Month #: '))
except:
    print('Error - invalid whole number entered.')

try:
    day = int(input('Enter Day #'))
except ValueError:
    print('Error - invalid whole number entered.')

try:
    year = int(input('Enter Year(YYYY): '))
except ValueError as ve:
    print('Error - invalid whole number entered.')
    print(ve)

print(f'{year}-{month}-{day}')


print('Bye')
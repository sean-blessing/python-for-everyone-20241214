print('Welcome to Control Statements')

# traffic light example
# red - stop
# yellow - slow down
# green - stop
# x - exit app

light_color = ''
while light_color != 'x':
    light_color = input('light color? ').lower()
    if light_color == 'red':
        print('Stop!')
    elif light_color == 'yellow':
        distance = int(input('Distance to light? '))
        if distance >= 20:
            print('Slow Down')
        else:
            print('Floor it!!!')
    elif light_color == 'green':
        print('Go!')
    elif light_color == 'x':
        pass
    else:
        print('Invalid color.')

# while statement - evaluating 'choice' continue statement
choice = 'y'
while choice == 'y':
    nbr1 = int(input('enter a whole number: '))
    print(f'you entered: {nbr1}')
    choice = input('Continue? (y/n) ').lower()
print('Bye')
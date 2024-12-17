print('Hello')

number = int(input('Enter a number: '))

choice = 'y'
while True:
    price = float(input("Price: "))
    quantity = int(input('Qty: '))
    total = price * quantity
    print(f'total: {total}')
    choice = input("Continue? ")
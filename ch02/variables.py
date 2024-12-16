print('Hello World!')

# define some variables
first_name = 'George'
price = 19.99
quantity = 3
tax = .065

print(price)

print('Hello, '+ first_name)
print('The price is: '+str(price))

total = (price * quantity) * (1 + tax)

print(f'The total is: {round(total, 2)}')

nbr1 = 23
nbr2 = 5

print(f'23 / 5 = {nbr1/nbr2}')
print(f'23 // 5 = {nbr1//nbr2}')
print(f'23 % 5 = {nbr1%nbr2}')

print(f'5**4: {nbr2**4}')
print(f'pow(5,4): {pow(nbr2, 4)}')

count = 0

print(f'count = {count}')
count = count + 1
print(f'count = {count}')
count += 1
print(f'count = {count}')
count += 10
print(f'count = {count}')
count -=5
print(f'count = {count}')
count*=10
print(f'count = {count}')

print('This is a really \treally long sentence.\nAre we done yet?')
print('Sally O\'Malley')
print("Sally O'Malley")
print('This is an implicit '+
      'continuation of a string')

print('a', end=' ')
print('b', end=' ')
print('c')

print(1,2,3,"a",4,5, sep="|")

print("Bye")
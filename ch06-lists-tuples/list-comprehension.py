print('Welcome to List Comprehension')

numbers = [1, 2, 3, 4, 5, 6]
print(f'numbers: {numbers}')

squares = []
for n in numbers:
    squares.append(n*n)
print(f'squares: {squares}')

print('-- list comprehension --')
cubed = [n*n*n for n in numbers]
print(f'cubed: {cubed}')

even_squares = [n*n for n in numbers if n % 2 == 0]
print(f'even_squares = {even_squares}')

# generate a list 1 to 10
list1 = [n+1 for n in range(10)]
print(list1)

print('Bye')
print('Welcome to Lists')

books = ["The Hobbit", "Lord of the Rings", "Harry Potter and the Sorcer's Stone"]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
prices = [19.99, 76.49, 1.50, 10.00]
things = ["ball", 5, 7.99, "message"]

# * operator to create list
numbers = [0] * 10

print(f'numbers: {numbers}')
print(f'books: {books}')

# get items from the list
print(f'book 0: {books[0]}')
print(f'book 1: {books[1]}')
print(f'book 2: {books[2]}')

# append, insert(index, item), remove(item), index(item), pop([index])
books.append('Atomic Habits')
print(f'1 books: {books}')
books.insert(2, "Hitchhiker's Guide to the Galaxy")
print(f'2 books: {books}')
books.remove('The Hobbit')
print(f'3 books: {books}')
removed_book = books.pop(1)
print(f'4 books: {books}')
print(f'removed_book = {removed_book}')
print(f'5 books: {books}')
idx = books.index('Lord of the Rings')
#idx2 = books.index('asdf')
print(idx)
# len
print(f'How many items in list? {len(books)}')

# check for existence - in keyword
print(f'abc exists? {'abc' in books}')
print(f'Atomic Habits exists? {'Atomic Habits' in books}')

# loop thru list - for in range (use len)
for i in range(3):
    print(f'books[{i}] = {books[i]}')
for i in range(len(books)):
    print(f'books[{i}] = {books[i]}')

# loop thru list - for item in list
print('-'*20)
for book in books:
    print(f'Book = {book}')
print('for loop with enumerate():')
for idx, book in enumerate(books):
    print(f'books[{idx}] = {book}')
# zip - slide 24

# 2 dimensional lists, list of lists, slide 30
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]
]
print(f'two_d_list: {two_d_list}')
for row in two_d_list:
    for col in row:
        print(col, end=" ")
    print()

# sort a list
print("= " *10)
print(prices)
print(f'sorted prices: {sorted(prices)}')
prices.sort()
print(f'prices.sort(): {prices}')
prices.reverse()
print(f'prices.reverse(): {prices}')

print("= "*10)
fruits = ['orange', 'apple', 'Pear', 'banana']
print(f'fruits = {fruits}')
print(f'sorted fruits: {sorted(fruits)}')
print(f'sorted fruits (key): {sorted(fruits, key=str.lower)}')
print(f'fruits = {fruits}')
print("= "*10)
fruits.sort()
print(f'fruits.sort = {fruits}')
fruits.sort(key=str.lower)
print(f'fruits.sort2 = {fruits}')
print("= "*10)
print(prices)
print(f'min: {min(prices)}')
print(f'max: {max(prices)}')
print(f'sum: {sum(prices)}')

import statistics
print(f'min: {statistics.mean(prices)}')

print('* '*10)
print(f'prices: {prices}')
print(f'prices[0:3] = {prices[0:3]}')
print(f'prices[:2] = {prices[:2]}')
print(f'prices[3:] = {prices[3:]}')
print(f'prices[::-1] = {prices[::-1]}')

print('Bye')
print('Welcome to the String Processor')

message = "Hello out there!"
print(f'message[0]: {message[0]}')
print(f'message[1]: {message[1]}')
print(f'message[-1]: {message[-1]}')
#print(f'message[16]: {message[16]}')
# message[0] = "J" -> can't change a string

message = "Hello out there!!!"
message += "!!!!!"
print(message)

print(f'message[:5]: {message[:5]}')
print(f'message[6:9]: {message[6:9]}')
print(f'message[10:]: {message[10:]}')
print(f'message[:-1]: {message[:-1]}')

query = '''SELECT *
           FROM Product P
           JOIN LineItem LI ON LI.ProductId = P.ProductId
           '''
print(f'query = {query}')

# does message contain the word 'out'?
print(f"out in message?: {'out' in message}")

print(f'message = {message}')
for char in message:
    print(f'char - {char}')

print('='*20)

# read the file, read each line, and split line into a list
with open('./ch10/files/movies.csv') as file_in:
    for line in file_in:
        line = line.rstrip()
        fields = line.split(",")
        print(f'fields: {fields}')
        print(f'Movie Summary: {fields[0]} ({fields[1]}), rated {fields[2]}')

print('\n p. 288 joining strings')
first = "Bob"
middle = "Nathan"
last = "Jones"

fullname_1 = first + " " + middle + " " + last
print(f'fullname_1 = {fullname_1}')

fullname_2 = first
fullname_2 += " " + middle
fullname_2 += " " + last
print(f'fullname_2 = {fullname_2}')

fullname_3 = f"{first} {middle} {last}"
print(f'fullname_3 = {fullname_3}')

names = ['Sean', 'Anjana', 'Andrew', 'Vineesh']
delimiter = "|"
joined_names = delimiter.join(names)
print(f'joined_names = {joined_names}')

print('Bye')
print('Welcome to File IO')

FILE_NAME = './ch07-file-io/files/test.txt'
print('Write string literat to file')
with open(FILE_NAME, "w") as file_out:
    file_out.write("Sean\tInstructor\nAnjana\t"+
                   "Student 1\nVineesh\tStudent 2\nAndrew\tStudent 3")

print('Write list of strings to file - writelines')
people = ['Sean\n', 'Anjana\n', 'Vineesh\n', 'Andrew\n']
with open(FILE_NAME, "w") as file_out:
    file_out.writelines(people)

print('Write list of strings to file - for loop & write')
people = ['Sean', 'Anjana', 'Vineesh', 'Andrew', 'Test']
with open(FILE_NAME, "w") as file_out:
    for person in people:
        file_out.write(person+"\n")

print('= '*10)
print('Read test.txt')
with open(FILE_NAME) as file_in:
    for line in file_in:
        print(line, end="")
print('Read test.txt - entire file as string')
with open(FILE_NAME) as file_in:
    contents = file_in.read()
    print(contents)
print('Read file as list')
with open(FILE_NAME) as file_in:
    people = file_in.readlines()
    print(people)

print('Read file by line, strip new line')
with open(FILE_NAME) as file_in:
    people = file_in.readlines()
    for person in people:
        #person = person.rstrip()
        #person = person[:-1]
        person = person.replace("\n", "")
        print(person)


print('Bye')
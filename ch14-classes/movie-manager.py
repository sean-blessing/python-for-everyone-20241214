from movie import Movie

movies_list = []
FILE_NAME = './ch14-classes/files/movies.txt'
DELIM = "\t"

def write_movies():
    with open(FILE_NAME, "w") as file_out:
        for movie in movies_list:
            file_out.write(movie.title+DELIM)
            file_out.write(str(movie.year)+DELIM)
            file_out.write(movie.rating+DELIM)
            file_out.write(movie.director)
            file_out.write("\n")

def read_movies():
    with open(FILE_NAME) as file_in:
        for line in file_in:
            fields = line.rstrip().split(DELIM)
            title, year, rating, director = fields
            movie = Movie(title, year, rating, director)
            movies_list.append(movie)

def display_menu():
    print('COMMAND MENU:')
    print('list - list movies')
    print('add  - add movie')
    print('exit - exit app')

def list_movies():
    print("\nMovies List:")
    print("="*15)
    if len(movies_list) == 0:
        print('No Movies yet. Add some.')
    else:
        print(f"{'Title':25}{'Year':10}{'Rating':10}{'Director':25}")
        for movie in movies_list:
            print(f'{movie.title:25}{movie.year:<10}{movie.rating:10}{movie.director:25}')

def add_movie():
    print("\nAdd a Movie:")
    print("="*15)
    title = input('Title: ')
    year = int(input("Release Year: "))
    rating = input("Age Rating: ")
    director = input("Director: ")
    movie = Movie(title, year, rating, director)
    movies_list.append(movie)
    print('Movie added.')
    write_movies()

def main():
    movies_list = read_movies()
    print("Welcome to the movie manager")
    print()
    command = ''
    while command != 'exit':
        display_menu()
        command = input('Command: ')
        match command:
            case 'list':
                list_movies()
            case 'add':
                add_movie()
            case 'exit':
                pass
            case '_':
                print("Invalid command. Try again.")

    print("Bye")

if __name__ == "__main__":
    main()
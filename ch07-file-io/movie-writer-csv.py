import csv

FILE_NAME = './ch07-file-io/files/movies.csv'

# create initial movie list
# movie1 = ['Star Wars', 1977, 'PG', 'George Lucas']
# movie2 = ['E.T.', 1982, 'PG', 'Steven Spielberg']
# movie3 = ['Red One', 2024, 'PG-13', 'Jake Kasdan']
# movies_list = [movie1, movie2, movie3]

def write_movies(movies):
    with open(FILE_NAME, 'w', newline='') as file_out:
        writer = csv.writer(file_out)
        writer.writerows(movies)

def read_movies():
    movies = []
    with open(FILE_NAME, newline="") as file_in:
        reader = csv.reader(file_in)
        for row in reader:
            movies.append(row)
    return movies

def main():
    print('Welcome to the Movie Writer - CSV Edition')
    # initialize list of movies
    movies_list = read_movies()
    command = ''
    while command != 'exit':
        print('Movie Options:')
        print('list - list movies')
        print('add  - add a movie')
        print('exit - exit app')
        print()
        command = input('Command? ')
        match command:
            case 'list':
                print('\n---- List Movies ----')
                for movie in movies_list:
                    print(movie)
            case 'add':
                print('\n---- Add Movie ----')
                # prompt for new movie
                title = input('Movie Title: ')
                year = int(input('Release Year: '))
                rating = input('Age Rating: ')
                director = input('Director: ')
                movie = [title, year, rating, director]
                # add movie to list
                movies_list.append(movie)
                # write movie csv
                write_movies(movies_list)
            case 'exit':
                pass
            case'_':
                print('\nInvalid Command')
            

    
    
    print('Bye')

if __name__ == '__main__':
    main()
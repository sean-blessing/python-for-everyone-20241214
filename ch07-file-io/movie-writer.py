import csv

FILENAME = './ch07-file-io/files/movies.csv'

# movie1 = ['Star Wars Episode IV: A New Hope', 1977, 'PG', 'George Lucas']
# movie2 = ['E.T.', 1982, 'PG', 'Steven Spielberg']
# movie3 = ['Red One', 2024, 'PG-13', 'Jake Kasdan']

# movies = [movie1, movie2, movie3]

def write_movies(movies):
    with open(FILENAME, 'w', newline="") as file_out:
        writer = csv.writer(file_out)
        writer.writerows(movies)

def read_movies():
    movies = []
    with open(FILENAME, newline="") as file_in:
        reader = csv.reader(file_in) 
        for row in reader: movies.append(row)
    return movies

def main():
    print('Welcome to the Movie Writer App')
    movies = read_movies()
    for movie in movies:
        print(movie)
    print('Bye')

if __name__ == '__main__':
    main()
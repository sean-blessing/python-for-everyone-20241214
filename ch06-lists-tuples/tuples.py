print('Welcome to tuples')

# Movie: Star Wars: Episode IV: A New Hope
#       1977, PG, George Lucas
title = input('Movie Title: ')
year = int(input('Release Year: '))
rating = input('Age Rating: ')
director = input('Director: ')

movie_tuple = title, year, rating, director

print(f'Movie: {movie_tuple}')

print(f'movie_tuple[0]: {movie_tuple[0]}')
print(f'movie_tuple[1]: {movie_tuple[1]}')
print(f'movie_tuple[2]: {movie_tuple[2]}')
print(f'movie_tuple[3]: {movie_tuple[3]}')

# unpacking a tuple
tuple_values = (1, 2, 3)
jan, feb, mar = tuple_values
print(f'jan: {jan}')

print('bye')
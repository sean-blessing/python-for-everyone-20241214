print('Welcome to the Movie Dictionary App')

movies_dict = {
    1: {
        "title": "Star Wars Episode IV: A New Hope",
        "year": 1977,
        "rating": "PG",
        "director": "George Lucas"
    },
    2: {
        "title": "E.T.",
        "year": 1982,
        "rating": "PG",
        "director": "Steven Spielberg"    
    },
    3: {
        "title": "Red One",
        "year": 2024,
        "rating": "PG-13",
        "director": "Jake Kasdan"
    }
}

print(f'movies_dict: {movies_dict}')

print('Add a movie:')
title = input('Title: ')
year = int(input("Release Year: "))
rating = input("Age Rating: ")
director = input("Director: ")

# generate an id - max of all IDs +1
new_movie_id = max(movies_dict.keys()) + 1

movies_dict[new_movie_id] = { "title": title, "year": year, "rating": rating, "director": director}

print(f'movies_dict: {movies_dict}')

print('Bye')
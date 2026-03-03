favorite_movies = [
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    }
]

print(favorite_movies)

total_favorite_movies = len(favorite_movies)
print("How many total favorite movies do we have?", total_favorite_movies)

print(type(favorite_movies), type(favorite_movies[0]))

print("Enter your favorite movie of the last year:")
recent_favorite_movie = input()
print("Your favorite movie is of the last year:", recent_favorite_movie)
favorite_movies_exercise = [
    {
        "name": "Inception",
        "release_year": 2010,
        "sequels": []
    }
]

favorite_books = [
    {
        "name": "The Alchemist",
        "release_year": 1988,
        "series": []
    }
]

print("Enter a long description of your favorite movie:")
movie_description = input()
favorite_movies_exercise[0]["long_description"] = movie_description

print("Enter a long description of your favorite book:")
book_description = input()
favorite_books[0]["long_description"] = book_description

movie_words = favorite_movies_exercise[0]["long_description"].split(" ")
book_words = favorite_books[0]["long_description"].split(" ")

favorite_movies_exercise[0]["short_description"] = " ".join(movie_words[:10])
favorite_books[0]["short_description"] = " ".join(book_words[:10])

print("Number of favorite movies:", len(favorite_movies_exercise))
print("Number of favorite books:", len(favorite_books))

print("Short movie description:", favorite_movies_exercise[0]["short_description"])
print("Short book description:", favorite_books[0]["short_description"])

print("Length of movie long description:", len(movie_words))
print("Length of book long description:", len(book_words))



num_movies = int(input("How many favorite movies would you like to enter? "))

favorite_movies = []

for i in range(num_movies):
    name = input("Enter movie name: ")
    year = int(input("Enter release year: "))
    favorite_movies.append((name, year))

def check_movie(movie):
    name = movie[0]
    year = movie[1]

    if year < 2000:
        print(name + " was released before 2000.")
    else:
        print(name + " was released after 2000.")
        return name

recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)

    if result is not None:
        recent_movies.append(result)

print("Movies released after 2000:")
print(recent_movies)
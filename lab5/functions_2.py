# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# task 1
def is_imdb_above_5_5(movie):
    return movie["imdb"] > 5.5

# task 2
def get_high_imdb_movies(movie_list):
    return [m for m in movie_list if is_imdb_above_5_5(m)]

# task 3
def get_movies_by_category(movie_list, category):
    return [m for m in movie_list if m["category"] == category]

# task 4
def average_imdb_score(movie_list):
    total_score = sum(m["imdb"] for m in movie_list)
    return total_score / len(movie_list) if len(movie_list) > 0 else 0

# task 5
def average_imdb_score_by_category(movie_list, category):
    category_movies = get_movies_by_category(movie_list, category)
    return average_imdb_score(category_movies) if category_movies else 0

# Example usage
print(is_imdb_above_5_5(movies[0]))
print(get_high_imdb_movies(movies))
print(get_movies_by_category(movies, "Romance"))
print(average_imdb_score(movies))
print(average_imdb_score_by_category(movies, "Suspense"))

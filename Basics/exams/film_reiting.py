import sys

num_of_movies = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize
name_of_max = ""
name_of_min = ""
sum_raiting = 0
for i in range (num_of_movies):
    movie_name = input()
    raiting = float(input())
    if raiting < min_num:
        min_num = raiting
        name_of_min = movie_name

    if raiting > max_num:
        max_num = raiting
        name_of_max = movie_name
    sum_raiting += raiting
avarage_raiting = sum_raiting / num_of_movies
print(f"{name_of_max} is with highest rating: {max_num}")
print(f"{name_of_min} is with lowest rating: {min_num}")
print(f"Average rating: {avarage_raiting:.1f}")
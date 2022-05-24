import math

name_of_movie = input()
length_of_movie = float(input())
lunch_break = float(input())

time_for_lunch = lunch_break / 8
time_for_rest = lunch_break / 4

total_rest_time = time_for_lunch + time_for_rest
difference = abs(lunch_break - total_rest_time)
time_left = abs(difference - length_of_movie)
time_left = math.ceil(time_left)
if difference >= length_of_movie:
    print(f"You have enough time to watch {name_of_movie} and left with {time_left} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {time_left} more minutes.")
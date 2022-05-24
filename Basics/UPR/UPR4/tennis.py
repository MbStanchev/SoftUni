import math

num_of_turnaments = int(input())
starting_points = int(input())
points = 0
final_points = 0
wins = 0
for i in range (num_of_turnaments):
    stage_reached = input()
    if stage_reached == "W":
        points += 2000
        wins += 1
    elif stage_reached == "F":
        points += 1200
    elif stage_reached == "SF":
        points += 720

average_points = points / num_of_turnaments
final_points = starting_points + points
prosent_won = wins / num_of_turnaments *100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{prosent_won:.2f}%")

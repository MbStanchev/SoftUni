num_of_balls = int(input())

red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other = 0
points = 0
for i in range (num_of_balls):
    colors = input()
    if colors == "red":
        points += 5
        red_balls += 1
    elif colors == "orange":
        points += 10
        orange_balls += 1
    elif colors == "yellow":
        points += 15
        yellow_balls += 1
    elif colors == "white":
        points += 20
        white_balls += 1
    elif colors == "black":
        points = points / 2
        black_balls += 1
    else:
        other += 1
print(f"Total points: {int(points)}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black_balls}")
import math

x = int(input())
y = float(input())
z = int(input())
num_of_workers = int(input())

all_grapes = x * y * 0.4
for_wine = all_grapes / 2.5
difference = abs(z - for_wine)
wine_per_worker = difference / num_of_workers

if for_wine < z:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(for_wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
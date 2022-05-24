import math

num_day = int(input())
all_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

needed_food = math.ceil(num_day * (dog_food + cat_food + (turtle_food / 1000)))
difference = abs(math.ceil(all_food - needed_food))

if all_food >= needed_food:
    print(f"{difference} kilos of food left.")
else:
    print(f"{difference} more kilos of food are needed.")
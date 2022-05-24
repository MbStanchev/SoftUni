flowers = input()
nub_of_flowers = int(input())
budget = int(input())

price_of_Roses = 5
price_of_Dahlias = 3.8
price_of_Tulips = 2.8
price_of_Narcissus = 3
price_of_Gladiolus = 2.5

price_of_flowers = 0

if flowers == "Roses":
    price_of_flowers = nub_of_flowers * price_of_Roses
    if nub_of_flowers > 80:
        price_of_flowers = 5 * 0.9
    else:
        price_of_flowers = 5

elif flowers == "Dahlias":
    if nub_of_flowers > 90:
        price_of_flowers = 3.8 * 0.85
    else:
        price_of_flowers = 3.8

elif flowers == "Tulips":
    if nub_of_flowers > 80:
        price_of_flowers = 2.8 * 0.85
    else:
        price_of_flowers = 2.8

elif flowers == "Narcissus":
    if nub_of_flowers < 120:
        price_of_flowers = 3 * 1.15
    else:
        price_of_flowers = 3

elif flowers == "Gladiolus":
    if nub_of_flowers < 80:
        price_of_flowers = 2.5 * 1.2
    else:
        price_of_flowers = 2.5

cost = nub_of_flowers * price_of_flowers
difference = abs(budget - cost)
if budget >= cost:
    print(f"Hey, you have a great garden with {nub_of_flowers} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
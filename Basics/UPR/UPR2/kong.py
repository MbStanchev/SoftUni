bugget = float(input())
decor = bugget * 0.1
num_statist = int(input())
price_of_one_dress = float(input())

price_of_all_dress = num_statist * price_of_one_dress

if num_statist > 150:
    price_of_all_dress *= 0.9

total_cost = decor + price_of_all_dress
difference = abs(bugget - total_cost)

if total_cost > bugget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
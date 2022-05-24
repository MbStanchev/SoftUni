buget = float(input())
category = input()
num_of_people = int(input())
transport_cost = 0
ticket = 0

if category == "VIP":
    ticket = 499.99
else:
    ticket = 249.99

if num_of_people <= 4:
    transport_cost = buget * 0.75
elif 5 <= num_of_people <= 9:
    transport_cost = buget * 0.6
elif 10 <= num_of_people <= 24:
    transport_cost = buget * 0.5
elif 25 <= num_of_people <= 49:
    transport_cost = buget * 0.4
else:
    transport_cost = buget * 0.25

all_cost = transport_cost + (num_of_people * ticket)
diference = abs(buget - all_cost)

if buget >= all_cost:
    print(f"Yes! You have {diference:.2f} leva left.")
else:
    print(f"Not enough money! You need {diference:.2f} leva.")
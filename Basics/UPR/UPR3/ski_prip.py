days_of_stay = int(input())
type_of_room = input()
rate = input()

price = 0
nights = days_of_stay - 1

if type_of_room == "room for one person":
    price = nights * 18

elif type_of_room == "apartment":
    if days_of_stay < 10:
        price = nights * 25 * 0.7
    elif 10 <= days_of_stay <= 15:
        price = nights * 25 * 0.65
    else:
        price = nights * 25 * 0.5

elif type_of_room == "president apartment":
    if days_of_stay < 10:
        price = nights * 35 * 0.9
    elif 10 <= days_of_stay <= 15:
        price = nights * 35 * 0.85
    else:
        price = nights * 35 * 0.8

if rate == "positive":
    price = price + price * 0.25
else:
    price = price - price * 0.1
print(f"{price:.2f}")

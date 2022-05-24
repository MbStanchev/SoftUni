month = input()
spend_houers = int(input())
peple_per_group = int(input())
day_night = input()
price_h = 0
if day_night == "day":
    if month == "march" or month == "april" or month == "may":
        price_h = 10.50
    elif month == "june" or month == "july" or month == "august":
        price_h = 12.60

if day_night == "night":
    if month == "march" or month == "april" or month == "may":
        price_h = 8.40
    elif month == "june" or month == "july" or month == "august":
        price_h = 10.20

if peple_per_group >= 4:
    price_h = price_h * 0.9
if spend_houers >= 5:
    price_h = price_h * 0.5
total_price = (price_h * peple_per_group) * spend_houers

print(f"Price per person for one hour: {price_h:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")

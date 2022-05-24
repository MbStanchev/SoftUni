type_of_fuel = input()
quantety_of_fuel = float(input())
club_card = input()
price_of_fuel = 0
price1 = 2.22
price2 = 2.33
price3 = 0.93

if club_card == "Yes":
    if type_of_fuel == "Gasoline":
        price1 = price1 - 0.18
    elif type_of_fuel == "Diesel":
        price2 = price2 - 0.12
    elif type_of_fuel == "Gas":
        price3 = price3 - 0.08


if quantety_of_fuel < 20:
    if type_of_fuel == "Gasoline":
        price_of_fuel = quantety_of_fuel * price1
    elif type_of_fuel == "Diesel":
        price_of_fuel = quantety_of_fuel * price2
    elif type_of_fuel == "Gas":
        price_of_fuel = quantety_of_fuel * price3

elif 20 <= quantety_of_fuel <= 25:
    if type_of_fuel == "Gasoline":
        price_of_fuel = quantety_of_fuel * price1 * 0.92
    elif type_of_fuel == "Diesel":
        price_of_fuel = quantety_of_fuel * price2 * 0.92
    elif type_of_fuel == "Gas":
        price_of_fuel = quantety_of_fuel * price3 * 0.92

elif quantety_of_fuel > 25:
    if type_of_fuel == "Gasoline":
        price_of_fuel = quantety_of_fuel * price1 * 0.90
    elif type_of_fuel == "Diesel":
        price_of_fuel = quantety_of_fuel * price2 * 0.90
    elif type_of_fuel == "Gas":
        price_of_fuel = quantety_of_fuel * price3 * 0.90

print(f"{price_of_fuel:.2f} lv.")


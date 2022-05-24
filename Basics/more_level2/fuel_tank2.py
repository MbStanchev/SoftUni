type_of_fuel = input()
fuel_in_tank = float(input())
fuel = type_of_fuel.lower()

if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
    if fuel_in_tank >= 25:
        print(f"You have enough {fuel}.")
    elif fuel_in_tank < 25:
        print(f"Fill your tank with {fuel}!")
else:
    print(f"Invalid fuel!")

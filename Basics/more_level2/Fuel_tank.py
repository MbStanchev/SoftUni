type_of_fuel = input()
fuel_in_tank = float(input())
fuel = ""

if type_of_fuel != "Diesel" and type_of_fuel != "Gasoline" and type_of_fuel != "Gas":
    print(f"Invalid fuel!")
else:
    if fuel_in_tank >= 25:
        if type_of_fuel == "Diesel":
            fuel = "diesel"
        elif type_of_fuel == "Gasoline":
            fuel = "gasoline"
        elif type_of_fuel == "Gas":
            fuel = "gas"
        print(f"You have enough {fuel}.")
    else:
        if type_of_fuel == "Diesel":
            fuel = "diesel"
        elif type_of_fuel == "Gasoline":
            fuel = "gasoline"
        elif type_of_fuel == "Gas":
            fuel = "gas"
        print(f"Fill your tank with {fuel}!")






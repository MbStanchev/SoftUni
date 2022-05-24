nub_of_km = int(input())
day_night = input()
price = 0

if day_night == "day":

    if nub_of_km >= 100:
        price = 0.06 * nub_of_km

    elif nub_of_km >= 20:
        price = 0.09 * nub_of_km
    else:
        price = 0.7 + 0.79 * nub_of_km

elif day_night == "night":

    if nub_of_km >= 100:
        price = 0.06 * nub_of_km

    elif nub_of_km >= 20:
        price = 0.09 * nub_of_km
    else:
        price = 0.7 + 0.9 * nub_of_km

print(f"{price:.2f}")
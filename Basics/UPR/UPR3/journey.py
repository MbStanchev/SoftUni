buget = float(input())
season = input()

money_spent = 0
destination = ""
camp_hotel = ""

if buget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        camp_hotel = "Camp"
        money_spent = buget * 0.3
    elif season == "winter":
        camp_hotel = "Hotel"
        money_spent = buget * 0.7

elif buget <= 1000:
    destination = "Balkans"
    if season == "summer":
        camp_hotel = "Camp"
        money_spent = buget * 0.4
    elif season == "winter":
        camp_hotel = "Hotel"
        money_spent = buget * 0.8

elif buget > 1000:
    destination = "Europe"
    camp_hotel = "Hotel"
    money_spent = buget * 0.9

print(f"Somewhere in {destination}")
print(f"{camp_hotel} - {money_spent:.2f}")
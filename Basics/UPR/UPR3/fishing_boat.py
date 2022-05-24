buget = int(input())
season = input()
num_fisheerman = int(input())

boat_rent = 0
if season == "Spring":
    if num_fisheerman <= 6:
        boat_rent = 3000 * 0.9
    elif 7<= num_fisheerman <= 11:
        boat_rent = 3000 * 0.85
    elif num_fisheerman >= 12:
        boat_rent = 3000 * 0.75

if season == "Summer" or season == "Autumn":
    if num_fisheerman <= 6:
        boat_rent = 4200 * 0.9
    elif 7 <= num_fisheerman <= 11:
        boat_rent = 4200 * 0.85
    elif num_fisheerman >= 12:
        boat_rent = 4200 * 0.75

if season == "Winter":
    if num_fisheerman <= 6:
        boat_rent = 2600 * 0.9
    elif 7 <= num_fisheerman <= 11:
        boat_rent = 2600 * 0.85
    elif num_fisheerman >= 12:
        boat_rent = 2600 * 0.75

if num_fisheerman % 2 == 0 and season != "Autumn":
    boat_rent *= 0.95

difference = abs(boat_rent - buget)
if buget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
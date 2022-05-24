degice = int(input())
tim_of_day = input()
outfit = ""
shoes = ""

if tim_of_day == "Morning":
    if 10 <= degice <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degice <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degice >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif tim_of_day == "Afternoon":
    if 10 <= degice <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degice <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degice >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif tim_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {degice} degrees, get your {outfit} and {shoes}.")
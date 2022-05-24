month = input()
num_of_nights = int(input())

type_of_room = ""
cost_studio = 0
cost_apartment = 0

if month == "May" or month == "October":
    if num_of_nights > 14:
        type_of_room = "Apartment"
        cost_apartment = num_of_nights * 65 * 0.9
    else:
        type_of_room = "Apartment"
        cost_apartment = num_of_nights * 65

    if 7 < num_of_nights <= 14:
        type_of_room = "Studio"
        cost_studio = (num_of_nights * 50) * 0.95
    elif num_of_nights > 14:
        type_of_room = "Studio"
        cost_studio = (num_of_nights * 50) * 0.7
    else:
        type_of_room = "Studio"
        cost_studio = (num_of_nights * 50)

elif month == "June" or month == "September":
    if num_of_nights > 14:
        type_of_room = "Apartment"
        cost_apartment = num_of_nights * 68.7 * 0.9
    else:
        type_of_room = "Apartment"
        cost_apartment = num_of_nights * 68.7

    if num_of_nights > 14:
        type_of_room = "Studio"
        cost_studio = (num_of_nights * 75.20) * 0.8
    else:
        type_of_room = "Studio"
        cost_studio = (num_of_nights * 75.20)

elif month == "July" or month == "August":
    if num_of_nights > 14:
        type_of_room = "Apartment"
        cost_apartment = num_of_nights * 77 * 0.9
    else:
        type_of_room = "Apartment"
        cost_apartment = num_of_nights * 77

    if num_of_nights > 0:
        type_of_room = "Studio"
        cost_studio = num_of_nights * 76

print(f"Apartment: {cost_apartment:.2f} lv.")
print(f"Studio: {cost_studio:.2f} lv.")
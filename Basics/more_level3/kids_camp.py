season = input()
group_type = input()
num_of_students = int(input())
num_of_nights = int(input())
room_price = 0
cost = 0
sport = ""
if group_type == "girls":
    if season == "Winter":
        room_price = 9.6
        sport = "Gymnastics"
    elif season == "Spring":
        room_price = 7.2
        sport = "Athletics"
    else:
        room_price = 15
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        room_price = 9.6
        sport = "Judo"
    elif season == "Spring":
        room_price = 7.2
        sport = "Tennis"
    else:
        room_price = 15
        sport = "Football"
elif group_type == "mixed":
    if season == "Winter":
        room_price = 10
        sport = "Ski"
    elif season == "Spring":
        room_price = 9.5
        sport = "Cycling"
    else:
        room_price = 20
        sport = "Swimming"
if num_of_students < 10:
    cost = num_of_students * room_price * num_of_nights
elif 10 <= num_of_students < 20:
    cost = num_of_students * room_price * 0.95 * num_of_nights
elif 20 <= num_of_students < 50:
    cost = num_of_students * room_price * 0.85 * num_of_nights
elif num_of_students >= 50:
    cost = num_of_students * room_price * 0.5 * num_of_nights


print(f"{sport} {cost:.2f} lv.")
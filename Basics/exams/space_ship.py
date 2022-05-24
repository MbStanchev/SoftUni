import math

wide_ship = float(input())
lenght_ship = float(input())
hight_ship = float(input())
avarige_hight_of_astronafts = float(input())

volium_ship = wide_ship * lenght_ship * hight_ship
volium_room = (avarige_hight_of_astronafts + 0.4) * 2 * 2
ship_will_hold = volium_ship/volium_room
if ship_will_hold < 3:
    print(f"The spacecraft is too small.")
elif 3 <= ship_will_hold <= 10:
    print(f"The spacecraft holds {math.floor(ship_will_hold)} astronauts.")
else:
    print(f"The spacecraft is too big.")

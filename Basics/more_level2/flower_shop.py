import math

num_magn=int(input())
num_zomb=int(input())
num_roses=int(input())
num_kaktus=int(input())
price_of_gift=float(input())
tax = 0.95
price = (num_magn * 3.25 + num_zomb * 4 + num_roses * 3.5 + num_kaktus * 8)
all = (price * tax)
difference = abs(all - price_of_gift)

if all >= price_of_gift:

    difference = math.floor(difference)
    print(f"She is left with {difference} leva.")
else:
    difference = math.ceil(difference)
    print(f"She will have to borrow {difference} leva.")
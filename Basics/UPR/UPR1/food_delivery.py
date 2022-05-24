price_chiken_menu = 10.35
price_fish_menu = 12.40
price_Vegy_menu = 8.15
price_delivery = 2.50

chiken_menu = int(input())
fish_menu = int(input())
vegy_menu = int(input())

cost = chiken_menu * price_chiken_menu + fish_menu * price_fish_menu + vegy_menu * price_Vegy_menu
desert = cost * 20 / 100
total_cost = cost + desert + price_delivery
print(total_cost)
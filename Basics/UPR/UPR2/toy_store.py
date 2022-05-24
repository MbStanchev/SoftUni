price_puzzel = 2.6
price_dole = 3
price_bear = 4.1
price_minion = 8.2
price_truck = 2
price_trip = float(input())
num_puzzel = int(input())
num_dole = int(input())
num_bears = int(input())
num_minion = int(input())
num_truck = int(input())

total_numb = num_puzzel + num_dole + num_bears + num_minion + num_truck

turn_over = price_puzzel * num_puzzel + price_dole * num_dole + price_bear * num_bears\
            + price_minion * num_minion + price_truck * num_truck

if total_numb >= 50:
    turn_over *= 0.75

earned_money = turn_over * 0.9 # - наем 0.1%
money = abs(price_trip - earned_money)

if earned_money >= price_trip:
    print(f"Yes! {money:.2f} lv left.")
else:
    print(f"Not enough money! {money:.2f} lv needed.")

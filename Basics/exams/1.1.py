import math

price_video = int(input())
price_conector = int(input())
price_elecricity_per_video = float(input())
profit_one_video = float(input())

price_all_video = price_video * 13
price_all_conectors = price_conector * 13
all_cost = price_all_conectors + price_all_video + 1000
clear_profit_per_video = profit_one_video - price_elecricity_per_video
all_profit_all_video = clear_profit_per_video * 13
return_profit = all_cost / all_profit_all_video
print(all_cost)
print(math.ceil(return_profit))
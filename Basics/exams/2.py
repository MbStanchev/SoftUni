money_per_day = float(input())
won_money_per_day = float(input())
all_cost = float(input())
price_of_gift = float(input())

profit_from_money_per_day = money_per_day * 5
profit_won = won_money_per_day * 5
all_profit = profit_won + profit_from_money_per_day
expences = all_profit - all_cost
diff = abs(price_of_gift - expences)
if price_of_gift <= expences:
    print(f"Profit: {expences:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")
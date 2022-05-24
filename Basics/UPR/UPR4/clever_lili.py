years = int(input())
price_of_washer = float(input())
price_for_toy = int(input())

money_from_toys = 0
money_from_precents = 0
num_of_toys = 0
money_left = 0

for i in range (1, years + 1):
    if i % 2 == 0:
        money_from_precents += 10
        money_left += money_from_precents - 1
    else:
        num_of_toys += 1

money_from_toys = num_of_toys * price_for_toy
all_money = money_from_toys + money_left
diff = abs(all_money - price_of_washer)

if all_money >= price_of_washer:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
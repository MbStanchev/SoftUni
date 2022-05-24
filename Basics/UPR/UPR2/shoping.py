buget = float(input())
num_videocard = int(input())
num_prosesors = int(input())
num_ram = int(input())

price_videocard = num_videocard * 250
price_prosesor = price_videocard * 0.35
price_ram = price_videocard * 0.1

total_price = price_videocard + (price_prosesor * num_prosesors) + (price_ram * num_ram)

if num_videocard > num_prosesors:
    total_price = total_price * 0.85
difference = abs(buget - total_price)
if buget >= total_price:
    print(f"You have {difference:.2f} leva left!")

else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
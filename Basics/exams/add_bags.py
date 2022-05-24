price_over_20 = float(input())
wheit_of_lugedj = float(input())
days_till_trip = int(input())
num_of_lugedj = int(input())

if wheit_of_lugedj < 10:
    price_for_lugedj = price_over_20 * 0.2
elif 10 <= wheit_of_lugedj <= 20:
    price_for_lugedj = price_over_20 * 0.5
else:
    price_for_lugedj = price_over_20

if days_till_trip > 30:
    price_for_lugedj = price_for_lugedj * 1.1
elif 7 <= days_till_trip <= 30:
    price_for_lugedj = price_for_lugedj * 1.15
elif days_till_trip < 7:
    price_for_lugedj = price_for_lugedj * 1.4
total = num_of_lugedj * price_for_lugedj
print(f"The total price of bags is: {total:.2f} lv.")
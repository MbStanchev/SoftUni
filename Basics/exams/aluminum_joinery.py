num_of_dogrami = int(input())
type_of_dogrami = input()
deliver = input()
single_price = 0
final_price = 0
no_good =False
if num_of_dogrami < 10:
    no_good = True

if type_of_dogrami == "90X130":
    single_price = 110
    if 30 < num_of_dogrami <= 60:
        single_price *= 0.95
    elif num_of_dogrami > 60:
        single_price *= 0.92

elif type_of_dogrami == "100X150":
    single_price = 140
    if 40 < num_of_dogrami <= 80:
        single_price *= 0.94
    elif num_of_dogrami > 80:
        single_price *= 0.90

elif type_of_dogrami == "130X180":
    single_price = 190
    if 20 < num_of_dogrami <= 50:
        single_price *= 0.93
    elif num_of_dogrami > 50:
        single_price *= 0.88

elif type_of_dogrami == "200X300":
    single_price = 250
    if 25 < num_of_dogrami <= 50:
        single_price *= 0.91
    elif num_of_dogrami > 50:
        single_price *= 0.86
if deliver == "With delivery":
    price = (single_price * num_of_dogrami) + 60
else:
    price = single_price * num_of_dogrami

if num_of_dogrami > 99:
    final_price = price * 0.96
else:
    final_price = price
if no_good:
    print("Invalid order")
else:
    print(f"{final_price:.2f} BGN")

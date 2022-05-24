num_of_orders = int(input())
total = 0

for i in range(num_of_orders):
    prise_capsul = float(input())
    days = int(input())
    needed_capsuls = int(input())

    if prise_capsul < 0.01 or prise_capsul > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif needed_capsuls < 1 or needed_capsuls > 2000:
        continue

    price = prise_capsul * days * needed_capsuls
    total += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total:.2f}")

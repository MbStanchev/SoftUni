input_line = input()
sum = 0
znak = True
while input_line != "NoMoreMoney":
    amount = float(input_line)
    if amount < 0:

        znak = False
        break

    sum += amount
    print(f"Increase: {amount:.2f}")

    input_line = input()
if znak == False:
    print("Invalid operation!")
print(f"Total: {sum:.2f}")

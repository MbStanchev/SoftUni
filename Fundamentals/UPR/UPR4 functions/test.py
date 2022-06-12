word = input()


dig_couter = 0
for i in word:
    if i.isdigit():
        dig_couter += 1
    if dig_couter > 2:
        print(True)
    else:
        print("Password must have at least 2 digits")


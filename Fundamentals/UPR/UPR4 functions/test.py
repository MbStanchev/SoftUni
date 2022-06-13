word = input()


dig_couter = 0
for char in word:
    if char.isdigit():
        dig_couter += 1
if dig_couter >= 2:
    print("y")
else:
    print("Password must have at least 2 digits")
    print("n")

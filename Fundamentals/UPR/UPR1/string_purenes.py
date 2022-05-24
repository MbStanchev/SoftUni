f = int(input())

for i in range (f):
    stings = input()
    for char in stings:
        if char == "," or char == "." or char == "_":
            print(f"{stings} is not pure!")
            break
    else:

        print(f"{stings} is pure.")
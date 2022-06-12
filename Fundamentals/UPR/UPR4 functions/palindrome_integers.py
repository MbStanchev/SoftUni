numbers = input().split(", ")

for num in numbers:
    #
    num_rev = "".join(reversed(num))
    if num == num_rev:
        print(True)
    else:
        print(False)
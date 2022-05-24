numN = int(input())

for i in range (1101, 10000):
    i_as_str = str(i)
    is_speshal = True
    for digit in i_as_str:
        if digit == "0":
            is_speshal = False
            break
        elif numN % int(digit) != 0:
            is_speshal = False
            break
    if is_speshal:

        print(i_as_str, end=" ")

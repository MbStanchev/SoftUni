num = int(input())
num1 = str(num)

special = True
for i in range(1 , num + 1):
    i = str(i)
    sum = 0
    for index in (i):
        index = int(index)
        sum += index
    # for index, digits in enumerate(i):
    #     digits = int(digits)
    #     sum += digits
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
# if special:
#     print(True)
# else:
#
#     print (False)


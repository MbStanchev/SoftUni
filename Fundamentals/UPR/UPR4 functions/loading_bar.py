num = int(input())
list = []
porcent = 0
if 0 <= num <= 90 and num % 10 == 0:
    porcent = num // 10
    list.append(porcent * "%")
    list.append((10 - porcent) * ".")

    print(f"{num}%",end=" ")
    print(f"[{''.join(list)}]")
    print("Still loading...")
else:
    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

    else:
        pass
#
# def calculate(num):
#     pr = (num // 10) * '%'
#     dot = (10 - (num // 10)) * '.'
#     if num < 100:
#         print (f'{num}% [{pr}{dot}]')
#         print('Still loading...')
#     else:
#         print (f'100% Complete!')
#         print('[%%%%%%%%%%]')
#
#
# data = int (input ())
# if 0 <= data <= 100:
#     if data % 10 == 0:
#         calculate (data)
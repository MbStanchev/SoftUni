num = int(input())

for i in range(num):
    f = int(input())
    if f % 2 != 0:
        print(f"{f} is odd!")
        break
else:
    print("All numbers are even.")

num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1, ):
    sum_even = 0
    sum_odd = 0
    i_str = str(i)
    for index, diget in enumerate(i_str):
        if index % 2 == 0:
            sum_odd += int(diget)
        else:
            sum_even += int(diget)

    if sum_even == sum_odd:
        print(i, end=" ")

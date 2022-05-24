num = int(input())

first_num = num % 10
second = num // 10 % 10
thurd = num // 100 % 100

for i in range(1, first_num + 1):

    for j in range(1, second + 1):

        for k in range(1, thurd + 1):
            total = i * j * k
            print(f"{i} * {j} * {k} = {total};")


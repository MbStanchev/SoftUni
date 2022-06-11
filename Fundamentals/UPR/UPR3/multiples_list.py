factor = int(input())
count = int(input())
list = []
for i in range(count):
    num = factor * (i + 1)
    list.append(num)
print(list)
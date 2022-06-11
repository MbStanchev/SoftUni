num = input()
list = num.split(", ")
count_of_beggers = int(input())
amount_for_all_beggers = []
for i in range(count_of_beggers):
    sum = 0
    for f in range(i, len(list), count_of_beggers):
        num = int(list[f])
        sum += num
    amount_for_all_beggers.append(sum)
print(amount_for_all_beggers)
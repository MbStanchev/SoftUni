n = int(input())
count_positives = 0
sum_of_negatives = 0
lis_1 = []
lis_2 = []
for i in range(n):
    num = int(input())
    if num < 0:
        lis_2.append(num)
        sum_of_negatives += num
    else:
        lis_1.append(num)
        count_positives += 1
print(lis_1)
print(lis_2)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
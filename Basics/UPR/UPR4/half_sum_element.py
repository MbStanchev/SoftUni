n = int(input())
sum = 0
current_num = 0
max_num = 0

for i in range (0, n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    sum += current_num

all_sum = sum - max_num
diff = abs(max_num - all_sum)
if max_num == all_sum:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {diff}")


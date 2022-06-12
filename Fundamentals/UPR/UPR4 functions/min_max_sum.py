numbers = input().split()
list = []

for num in numbers:
    list.append(int(num))
min_num = min(list)
max_num = max(list)
all_sum = sum(list)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {all_sum}")


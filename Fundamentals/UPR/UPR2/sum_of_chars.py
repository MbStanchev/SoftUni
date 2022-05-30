num_of_lines = int(input())
total_sum = 0
for i in range(num_of_lines):
    symbol = input()
    sum = ord(symbol)
    total_sum += sum
print(f"The sum equals: {total_sum}")
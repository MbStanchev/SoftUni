n = int(input())

left_sum = 0
right_sum = 0

for i in range (0 , n):
    sik = int(input())
    left_sum += sik

for i in range (0 , n):
    sik = int(input())
    right_sum += sik
diff= abs(right_sum - left_sum)

if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {diff}")
num = int(input())

even = 0
odd = 0

for i in range (0, num):
    sink  = int(input())
    if i % 2 ==0:
        even += sink
    else:
        odd += sink
diff = abs(even - odd)

if even == odd:
    print("Yes")
    print(f"Sum = {even}")
else:
    print("No")
    print(f"Diff = {diff}")
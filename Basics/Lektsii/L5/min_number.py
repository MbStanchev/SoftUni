import sys

num = input()
min_size = sys.maxsize

while num != "Stop":
    current_nub = int(num)
    if current_nub < min_size:
        min_size = current_nub

    num = input()

print(min_size)

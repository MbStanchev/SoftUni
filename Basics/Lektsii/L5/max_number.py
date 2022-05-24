import sys

line = input()
max_size = -sys.maxsize
while line != "Stop":
    current_num = int(line)
    if current_num > max_size:
        max_size = current_num


    line = input()
print(max_size)
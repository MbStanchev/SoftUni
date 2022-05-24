start = int(input())
stop = int(input())
magic_num = int(input())
counter = 0
sum = 0
equual = False
for i in range (start, stop + 1):
    for j in range (start, stop + 1):
        sum = i + j
        counter += 1
        if sum == magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {sum})")
            equual = True
            break

    if equual:
        break
if not equual:
    print(f"{counter} combinations - neither equals {magic_num}")

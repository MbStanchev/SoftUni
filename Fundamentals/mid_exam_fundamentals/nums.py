sequence_of_integers = list(map(int, input().split()))
counter = 0
lst = []
average = sum(sequence_of_integers)/len(sequence_of_integers)
true = True
while counter < 5:
    max_num = max(sequence_of_integers)
    if max_num > average:
        lst.append(max_num)
        sequence_of_integers.remove(max_num)
        counter += 1

    else:
        if len(lst) == 0:
            true = False
            print("No")
            break
        else:
            break
if true:
    print(' '.join(str(num) for num in lst))
sequence_integers = input().split()
int_seq = [int(num) for num in sequence_integers]
command = input()
count = 0
while command != 'End':
    check_list = []
    index = int(command)
    if 0 <= index < len(int_seq) and index not in check_list:
        target = int_seq[index]
        int_seq[index] = -1
        check_list.append(index)
        count += 1
        for i in range(len(int_seq)):
            if target >= int_seq[i] != -1:
                int_seq[i] += target
            elif target < int_seq[i] != -1:
                int_seq[i] -= target
    else:
        pass

    command = input()
targets = ' '.join(str(num) for num in int_seq)
print(f"Shot targets: {count} -> {targets}")
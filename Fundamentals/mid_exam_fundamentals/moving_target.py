sequence_of_targets = list(map(int, input().split()))
lsi = sequence_of_targets.copy()
command = input().split()

while command[0] != "End":
    if command[0] == "Shoot":
        if int(command[1]) in range(0, len(sequence_of_targets)+1):
            index = int(command[1])
            power = int(command[2])
            if sequence_of_targets[index] - power <= 0:
                sequence_of_targets.pop(index)
            else:
                sequence_of_targets[index] -= power
        # else:
        #     print("Invalid placement!")

    elif command[0] == "Strike":
        lsi = sequence_of_targets.copy()
        inde = int(command[1])
        radius = int(command[2])
        if inde - radius >= 0 and inde + radius < len(sequence_of_targets):
            f = inde - radius
            s = inde + radius
            for i in range(f, s + 1):
                sequence_of_targets.remove(lsi[i])
        else:
            print("Strike missed!")

    elif command[0] == "Add":
        if 0 <= int(command[1]) < len(sequence_of_targets):
            index_1 = int(command[1])
            value = int(command[2])
            sequence_of_targets.insert(index_1, value)
        else:
            print("Invalid placement!")
    command = input().split()
print("|".join(str(num) for num in sequence_of_targets))

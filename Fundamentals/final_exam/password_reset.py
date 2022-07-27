command = input()
data = input()
lis = ''
empty = ''
while data != 'Done':
    entry = data.split()

    if entry[0] == 'TakeOdd':
        for i in range(1, len(command),2):
            lis += command[i]
        print(lis)
        command = lis

    elif entry[0] == 'Cut':
        start = int(entry[1])
        count = int(entry[2])
        end = int(start + count)
        left = command[0:start]
        # for f in range(0, start):
        #     empty += command[f]
        right = command[end:len(command)]
        # for g in range(end, len(command)):
        #     empty += command[g]

        command = left+right
        print(command)

    elif entry[0] == 'Substitute':

        if entry[1] in command:
            command = command.replace(entry[1], entry[2])
            print(command)
        else:
            print('Nothing to replace!')
    data = input()
print(f"Your password is: {command}")
command = input().split()
entry = ''.join(command)
for index in range(len(entry)):
    if entry[index] == ':':
        print(f":{entry[index+1]}")

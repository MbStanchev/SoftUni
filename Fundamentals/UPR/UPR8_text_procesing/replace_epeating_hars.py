entry = input()
storage = entry[0]
result = ''
for i in range(len(entry)):
    if result == '':
        result = entry[0]
    if entry[i] != storage:
        result += entry[i]
        storage = entry[i]
    else:
        pass

print(result)
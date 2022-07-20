data = input()
power = 0
result = ''
for index in range(len(data)):
    if data[index] == '>':
        power += int(data[index+1])
        result += '>'
    elif data[index].isalpha() and power == 0:
        result += data[index]
    elif power != 0:
        power -= 1
print(result)
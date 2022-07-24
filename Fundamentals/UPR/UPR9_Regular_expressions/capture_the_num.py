import re
data = input()
l = []
while data:
    pattern = r'\d+'
    result = re.findall(pattern, data)

    if result:
        print(*result, sep=' ', end=' ')
    data = input()

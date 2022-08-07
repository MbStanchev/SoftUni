import re
num = int(input())
lst = []
command = ''
pattern = r'!([A-Z][a-z]{3,})!:\[([A-Za-z]{8,})\]'
for i in range(num):
    strings = input()
    matches = re.findall(pattern,strings)
    if len(matches) == 0:
        print("The message is invalid")
    matches = re.finditer(pattern,strings)

    for mach in matches:
        command = mach[1]
        for_translate = mach[2]
        for ch in for_translate:
            result = ord(ch)
            lst.append(result)
        print(f"{command}:", end=' ')
        for i in lst:
            print(i, end=' ')
        print()
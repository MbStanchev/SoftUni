import re
# pattern = r'\b_([A-Za-z0-9]+)\b'
# data = input()
# match = re.findall(pattern, data)
# print(*match, sep=',')

pattern = r'((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b'
data = input()

match = re.finditer(pattern, data)
match = [i.group() for i in match]
print(*match, sep=',')
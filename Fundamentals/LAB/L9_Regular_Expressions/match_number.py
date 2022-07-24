import re
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
data = input()
match = re.finditer(pattern,data)
match = [num.group() for num in match]
print(*match)


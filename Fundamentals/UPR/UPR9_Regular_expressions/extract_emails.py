import re
date = input()
pattern = r'(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+[\.-]?[a-zA-Z]+(\.[a-zA-Z]+)+'
matches = re.finditer(pattern, date)
matches = [match.group() for match in matches]
print(*matches, sep='\n')
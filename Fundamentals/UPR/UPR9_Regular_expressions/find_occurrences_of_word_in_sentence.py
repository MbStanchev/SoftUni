import re

data = input().lower()
to_compare = input().lower()
pattern = fr'\b{to_compare}\b'
match = re.findall(pattern, data, re.IGNORECASE)

print(len(match))
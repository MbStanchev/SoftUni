import re
pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
num = int(input())

for _ in range(num):
    data = input()
    match = re.match(pattern,data)
    if not match:
        print('Invalid barcode')
        continue
    dig = re.findall(r'\d+',data)
    if not dig:
        print('Product group: 00')
    else:
        print(f'Product group: {"".join(dig)}')
   
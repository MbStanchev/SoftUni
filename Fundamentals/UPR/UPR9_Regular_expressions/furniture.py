import re
data = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)\b'
fur = []
all = 0

while data != 'Purchase':

    match = re.search(pattern, data)
    # match = [el.group() for el in match]
    if match:
        furn = match[1]
        fur.append(furn)
        price = float(match[2])
        quantity = int(match[3])
        total_price = price * quantity
        all += total_price

    data = input()
print('Bought furniture:')
for i in fur:
    print(i)
print(f'Total money spend: {all:.2f}')
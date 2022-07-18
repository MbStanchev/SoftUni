command = input()
dict = {}
while command != 'End':
    company, ident_num = command.split(' -> ')
    if company not in dict:
        dict[company] = []

    if ident_num not in dict[company]:
        dict[company].append(ident_num)

    command = input()

for k,v in dict.items():
    print(f"{k}")
    for i in v:
        print(f'-- {"".join(i)}')
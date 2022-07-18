entry1 = input()
phonebook = {}
while '-' in entry1:
    entry = entry1.split('-')
    name = entry[0]
    num = entry[1]
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(num)
    entry1 = input()
entry2 = int(entry1)
for i in range(entry2):
    serched_contacts = input()
    if serched_contacts not in phonebook:
        print(f'Contact {serched_contacts} does not exist.')
    else:
        print(f'{serched_contacts} -> {"".join(phonebook[serched_contacts])}')

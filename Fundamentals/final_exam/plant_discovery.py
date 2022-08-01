num = int(input())
plants = {}
for _ in range(num):
    entry = input().split('<->')
    plant, rarity = entry[0], entry[1]
    plants[plant] = {'rarity': int(rarity), 'rating': []}
entry = input()

while entry != "Exhibition":
    splited_entry = entry.split(': ')
    command = splited_entry[0]
    info = splited_entry[1]
    about = info.split(' - ')
    curent_plant = about[0]

    if curent_plant not in plants:
        print('error')
        entry = input()
        continue
    if command == 'Rate':
        plants[curent_plant]['rating'].append(int(about[1]))

    elif command == 'Update':
        new_rarity = int(about[1])
        plants[curent_plant]['rarity'] = new_rarity

    elif command == 'Reset':
        plants[curent_plant]['rating'].clear()
    else:
        print('error')
    entry = input()
print('Plants for the exhibition:')
for printing_purposes in plants:

    if len(plants[printing_purposes]["rating"]) > 0 and sum(plants[printing_purposes]["rating"]) > 0:
        average_rating = sum(plants[printing_purposes]["rating"])/len(plants[printing_purposes]["rating"])
    else:
        average_rating = 0
    print(f'- {printing_purposes}; Rarity: {plants[printing_purposes]["rarity"]}; Rating: {average_rating:.2f}')
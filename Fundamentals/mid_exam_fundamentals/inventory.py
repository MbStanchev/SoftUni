journal = input().split(', ')
command = input()
while command != 'Craft!':
    to_do = command.split(' - ')

    what_to_do = to_do[0]
    item = to_do[1]

    if what_to_do == 'Collect':
        if item not in journal:
            journal.append(item)
    elif what_to_do == 'Drop':
        if item in journal:
            journal.remove(item)
    elif what_to_do == 'Combine Items':
        splited = item.split(':')
        old_item = splited[0]
        new_item = splited[1]
        if old_item in journal:
            journal.insert(journal.index(old_item) + 1, new_item)
    elif what_to_do == 'Renew':
        if item in journal:
            poped = journal.pop(journal.index(item))
            journal.append(poped)
    command = input()
print(', '.join(journal))
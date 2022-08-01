num = int(input())
pieces = {}
for i in range(num):
    data = input().split('|')
    pieces[data[0]] = {'composer': data[1], 'key': data[2]}
entry = input()
while entry != "Stop":
    split_entry = entry.split('|')
    command = split_entry[0]

    if command == 'Add':
        piece, composer, key = split_entry[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == 'Remove':
        piece = split_entry[1]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del pieces[piece]
            print(f"Successfully removed {piece}!")

    elif command == 'ChangeKey':
        piece, new_key = split_entry[1:]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

    entry = input()
for piece in pieces:
    print(f"{piece} -> Composer: {pieces[piece]['composer']}, Key: {pieces[piece]['key']}")
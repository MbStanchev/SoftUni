raw_key = input()
instructions = input()
while instructions != "Generate":
    to_do = instructions.split('>>>')
    command = to_do[0]

    if command == 'Contains':
        if to_do[1] in raw_key:
            print(f'{raw_key} contains {to_do[1]}')
        else:
            print("Substring not found!")

    elif command == 'Flip':
        start = int(to_do[2])
        end = int(to_do[3])
        if to_do[1] == 'Upper':
            raw_key = raw_key[:start] + raw_key[start:end].upper() + raw_key[end:]
            print(raw_key)
        elif to_do[1] == 'Lower':
            raw_key = raw_key[:start] + raw_key[start:end].lower() + raw_key[end:]
            print(raw_key)

    elif command == 'Slice':
        begins = int(to_do[1])
        to = int(to_do[2])
        raw_key = raw_key[:begins] + raw_key[to:]
        print(raw_key)

    instructions = input()
print(f'Your activation key is: {raw_key}')
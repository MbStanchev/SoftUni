hiden_msg = input()
strings = input()
while strings != "Reveal":
    to_do = strings.split(":|:")
    command = to_do[0]

    if command == 'InsertSpace':
        index = int(to_do[1])
        hiden_msg = hiden_msg[:index] + ' ' + hiden_msg[index:]
        print(hiden_msg)

    elif command == 'Reverse':
        substring = to_do[1]
        if substring not in hiden_msg:
            print("error")
        else:
            rev_sub = substring[::-1]
            hiden_msg = hiden_msg.replace(substring,'')
            hiden_msg = hiden_msg + rev_sub
            print(hiden_msg)

    elif command == 'ChangeAll':
        sub_str = to_do[1]
        replacement = to_do[2]

        if sub_str in hiden_msg:
            hiden_msg = hiden_msg.replace(sub_str, replacement)
            print(hiden_msg)

    strings = input()
print(f'You have a new text message: {hiden_msg}')
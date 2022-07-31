encrypted_message = input()
to_do = input()
while to_do != "Decode":

    split_message = to_do.split('|')
    command = split_message[0]

    if command == 'Move':
        num = int(split_message[1])
        encrypted_message = encrypted_message[num:] + encrypted_message[:num]

    elif command == 'Insert':
        position = int(split_message[1])
        encrypted_message = encrypted_message[:position] + split_message[2] + encrypted_message[position:]

    elif command == 'ChangeAll':
        orig = split_message[1]
        to_replace = split_message[2]
        if split_message[1] in encrypted_message:
            encrypted_message = encrypted_message.replace(orig,to_replace)

    to_do = input ()
print(f"The decrypted message is: {encrypted_message}")

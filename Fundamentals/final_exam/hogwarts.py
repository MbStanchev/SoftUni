to_decipher = input()
command = input()
while command != 'Abracadabra':
    splited = command.split(' ')
    camanda = splited[0]

    if camanda == 'Abjuration':
        to_decipher = to_decipher.upper()
        print(to_decipher)

    elif camanda == 'Necromancy':
        to_decipher = to_decipher.lower()
        print(to_decipher)

    elif camanda == 'Illusion':
        index = int(splited[1])
        letter = splited[2]
        a = len(to_decipher)
        if index > len(to_decipher):
            print('The spell was too weak.')
        else:
            to_decipher = to_decipher.replace(to_decipher[index],letter)
            print('Done!')
    elif camanda == 'Divination':
        f_string = splited[1]
        s_string = splited[2]
        # if f_string not in to_decipher:
        #     pass

        for n in range (len (f_string)):
            if f_string[n] in to_decipher:
                to_decipher = to_decipher.replace (f_string[n], s_string[n])
        print(to_decipher)

    elif camanda == 'Alteration':
        to_remove = splited[1]
        if to_remove not in to_decipher:
            pass
        else:
            to_decipher = to_decipher.replace(to_remove,'')
            print(to_decipher)
    else:
        print('The spell did not work!')




    command = input ()
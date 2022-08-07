capacity = int(input())
commands = input()
msg = {}

while commands != "Statistics":
    splited = commands.split('=')
    comanda = splited[0]
    if comanda == 'Add':
        username = splited[1]
        sent = int(splited[2])
        recived = int(splited[3])
        if username in msg:
            pass
        else:
            msg[username] = {'sent': sent, 'recived': recived}
#
    elif comanda == 'Message':
        sender = splited[1]
        receiver = splited[2]
        suma1 = 0
        suma2 = 0
        if sender in msg and receiver in msg:
            msg[sender]['sent'] += 1
            msg[receiver]['recived'] += 1
            suma1 = msg[sender]['sent'] + msg[sender]['recived']
            suma2 = msg[receiver]['sent'] + msg[receiver]['recived']
#
        if suma1 == capacity:
            del msg[sender]
            print(f'{sender} reached the capacity!')
        elif suma2 == capacity:
            del msg[receiver]
            print(f'{receiver} reached the capacity!')
#
    elif comanda == 'Empty':
        user = splited[1]
        if user == "All":
            msg.clear()
#
        else:
            del msg[user]
    commands = input()
print(f'Users count: {len(msg)}')
for user in msg:
    sum = msg[user]['sent'] + msg[user]['recived']
    print(f'{user} - {sum}')
num = int(input())
train = [0] * num
comand = input().split(" ")
while comand[0] != "End":

    if comand[0] == "add":
        train[-1] += int(comand[1])
    elif comand[0] == "insert":
       train[int(comand[1])]  += int(comand[2])
    elif comand[0] == "leave":
        train[int(comand[1])] -= int(comand[2])
    comand = input().split(" ")
print(train)
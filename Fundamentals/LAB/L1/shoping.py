buget = int(input())
comand = input()
counter = 0
while comand != "End":
    price = int(comand)
    counter += price
    if buget < counter:
        print("You went in overdraft!")
        break
    comand = input()
else:
    print('You bought everything needed.')

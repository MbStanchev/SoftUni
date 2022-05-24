basket = 1.5
wreath = 3.8
chocolate_bunny = 7

num_of_clients = int(input())
for i in range (num_of_clients):
    type_of_buy = input()
    counter = 0
    total_amount = 0
    prise = 0
    while type_of_buy != "Finish":
        if type_of_buy == "basket":
            total_amount += basket

        elif type_of_buy == "wreath":
            total_amount += wreath

        elif type_of_buy == "chocolate bunny":
            total_amount += chocolate_bunny
        counter +=1
        type_of_buy = input()
    print(total_amount)
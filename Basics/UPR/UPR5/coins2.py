change = float(input())
counter = 0
change_in_coins = int(change * 100)

while change_in_coins > 0:
    if change_in_coins >= 200:
        change_in_coins -= 200
        counter += 1
    elif change_in_coins >= 100:
        change_in_coins -= 100
        counter += 1
    elif change_in_coins >= 50:
        change_in_coins -= 50
        counter += 1

    elif change_in_coins >= 20:
        change_in_coins -= 20
        counter += 1
    elif change_in_coins >= 10:
        change_in_coins -= 10
        counter += 1
    elif change_in_coins >= 5:
        change_in_coins -= 5
        counter += 1
    elif change_in_coins >= 2:
        change_in_coins -= 2
        counter += 1
    elif change_in_coins >= 1:
        change_in_coins -= 1
        counter += 1

print(counter)
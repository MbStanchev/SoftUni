order = input()
amount = int(input())


def cal(drink,many):
    result = None
    if drink == "coffee":
        result = 1.5
    elif drink == "water":
        result = 1.00
    elif drink == "coke":
        result = 1.40
    elif drink == "snacks":
        result = 2.00
    return result


print(f"{cal(order, amount) * amount:.2f}")
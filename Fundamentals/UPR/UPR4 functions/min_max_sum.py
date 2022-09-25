def mini(lst):
    a = min(entry)
    return f'The minimum number is {a}'


def maxi(lst):
    b = max (entry)
    return f'The maximum number is {b}'


def suma(lst):
    c = sum (entry)
    return f'The sum number is: {c}'


# def all(lst):
#     mini(lst)
entry = list(map(int, input().split()))

print(mini(entry))
print(maxi(entry))
print(suma(entry))
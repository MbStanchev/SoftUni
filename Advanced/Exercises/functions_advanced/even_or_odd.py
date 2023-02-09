def even_odd(*args):
    even = []
    odd = []
    command = args[-1]
    for i in args[:-1]:
        if i % 2 == 0:
           even.append(i)
        else:
            odd.append(i)
    if command == 'even':
        return even
    else:
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
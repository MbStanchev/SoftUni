def even_odd_filter(**kwargs):
    numbs = {}
    for key, val in kwargs.items():
        if key == 'even':
            numbs[key] = [el for el in val if el % 2 == 0]
        else:
            numbs[key] = []
            for elem in val:
                if elem % 2 != 0:
                    numbs[key].append(elem)
    return dict(sorted(numbs.items()))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

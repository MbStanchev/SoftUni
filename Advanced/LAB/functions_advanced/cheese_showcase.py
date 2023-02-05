def sorting_cheeses(**kwargs):
    sorted_chees = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = []
    for k ,v in sorted_chees:
        v1 = sorted(v, reverse=True)
        result.append(k)
        result.extend([str(el) for el in v1])
    return '\n'.join(result)

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)



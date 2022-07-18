countries = input().split(', ')
capitals = input().split(', ')
di = {}
for i in range(0, len(countries)):
    di[countries[i]] = capitals[i]
for k, v in di.items():
    print(f'{k} -> {v}')
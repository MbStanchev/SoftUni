entry = input ().split (' ')
dict = {}
for i in range (0, len (entry), 2):
    product = entry[i]
    quantity = entry[i + 1]
    dict[product] = quantity

to_search = input().split()
for index in range(0, len(to_search)):
    if to_search[index] not in dict:
        print(f"Sorry, we don't have {to_search[index]}")
    else:
        print(f'We have {dict[to_search[index]]} of {to_search[index]} left')

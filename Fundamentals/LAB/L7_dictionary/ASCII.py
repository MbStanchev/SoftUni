entry = input().split(', ')

# for i in entry:
#     dick[i] = ord(i)
dick = {i:ord(i) for i in entry}
print(dick)
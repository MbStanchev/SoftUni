num = int(input())
dict = {}

for i in range (num):
    word = input()
    sino = input()
    if word not in dict:
        dict[word] = []
    dict[word].append(sino)
for r in dict:
    print(f'{r} - {", ".join(dict[r])}')

# for k, v in dict.items():
#     print(f'{k} - {" ".join(v)}')
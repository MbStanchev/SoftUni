entry = input().split()

# for word in entry:
#     if len(word) % 2 == 0:
#         print(word)
print(*[word for word in entry if len(word) % 2 == 0], sep='\n')
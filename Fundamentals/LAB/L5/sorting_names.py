names = input().split(", ")

sorted(names)
print(sorted(names, key= lambda i: (-len(i), i)))

word = input()
vowers = ["a", "o", "u", "e", "i"]
result = [i for i in word if i not in vowers]
print("".join(result))

word = input().split(" ")
palindrome = input()
lst = []
for i in word:
    if i == i[::-1]:
        lst.append(i)

print(lst)
print(f"Found palindrome {lst.count(palindrome)} times")
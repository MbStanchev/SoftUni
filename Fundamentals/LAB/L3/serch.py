n = int(input())
word = input()
list = []
list_2 =[]

for i in range(n):
    string = input()
    list.append(string)
new_list = list.copy()
for f in range(len(list)):
    other = list[f]
    # if word in other:
    #     list_2.append(other)
    #     print(list_2)
    if word not in other:
        new_list.remove(other)
print(list)
print(new_list)
f_list = input().split(", ")
s_list = input().split(", ")
linal = []
for i in f_list:
    for j in s_list:
        if i in j:
           linal.append(i)
           break
print(linal)
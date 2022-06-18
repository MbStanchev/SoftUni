# number = list(map(int, input().split(", ")))
# lst = []
# for i in range(len(number)):
#     if number[i] % 2 == 0:
#         lst.append(i)
# print(lst)
lis = list(map(int, input().split(".")))
lis[-1] += 1
qef = []
for i in lis:
    qef.append(str(i))
print(qef)
a = ".".join(qef)
print(a)
# list = "some"
# for i in range(len(list)):
#     print(list[i])
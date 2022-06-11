entry = list(map(int, input().split( )))
n = int(input())
# entry = list(map(int, enty))
str_list = []

for i in range(n):
    min_num = min(entry)
    entry.remove(min_num)
for f in entry:
    str_list.append(str(f))

result = ", ".join(str_list)
print(result)
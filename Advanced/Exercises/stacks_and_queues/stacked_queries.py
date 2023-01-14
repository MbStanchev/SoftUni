ss = []
n = int(input())
rev_ss = []
for _ in range(n):
    entry = input()
    push_command = entry.split()
    if push_command[0] == '1':
        num = push_command[1]
        ss.append(int(num))
    elif entry == '2' and ss:
        ss.pop()
    elif entry == '3' and ss:
        print(max(ss))
    elif entry == '4' and ss:
        print(min(ss))
while ss:
    el = ss.pop()
    if ss:
        print(el, end=', ')
    else:
        print(el)
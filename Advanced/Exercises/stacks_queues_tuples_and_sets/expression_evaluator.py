from collections import deque
string_expression = input().split()
result = 0
num = deque()
operators = "*", "+", "-", "/"
for ch in string_expression:
    if ch not in operators:
        num.append(int(ch))
    else:
        while len(num) > 1:
            f = num.popleft()
            s = num.popleft()
            if ch == '-':
                result = f - s
            elif ch == "+":
                result = f + s
            elif ch == "*":
                result = f * s
            elif ch == "/":
                result = f // s
            num.appendleft(result)
print(result)
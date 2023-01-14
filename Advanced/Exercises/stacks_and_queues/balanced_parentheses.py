sequence = input()
parentheses = []
balanced = False
for i in sequence:
    if i in '{[(':
        parentheses.append(i)
    # elif not parentheses:
    #     balanced = False
    #     break
    else:
        if len(parentheses) <= 0:
            balanced = False
            break
        if f'{parentheses.pop()}{i}' not in '(){}[]':
            balanced = False
            break
        else:
            balanced = True
if balanced:
    print('YES')
else:
    print('NO')
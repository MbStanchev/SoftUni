n = int(input())
invited = set()
for i in range(n):
    code_inv = input()
    invited.add(code_inv)
code_came = input()
while code_came != 'END':
    if code_came in invited:
        invited.discard(code_came)
    code_came = input()
print(len(invited))
print('\n'.join(sorted(invited)))

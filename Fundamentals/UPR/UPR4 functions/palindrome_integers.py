def is_the_same(lst):
    if lst == lst[::-1]:
        return True
    return False


entry = (input().split(', '))
for i in entry:
    if is_the_same(i):
        print(True)
    else:
        print(False)
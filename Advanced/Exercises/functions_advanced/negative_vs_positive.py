numbs = [int(x) for x in input().split()]


def some_numbs_neg(some_lst):
    neg = []

    for num in some_lst:
        if num < 0:
            neg.append(num)
    return sum(neg)


def some_num_poz(some_lst):
    poz = []
    for num in some_lst:
        if num > 0:
            poz.append(num)
    return sum(poz)


nega = some_numbs_neg(numbs)
pozi = some_num_poz(numbs)
print(nega)
print(pozi)
if abs(nega) > pozi:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
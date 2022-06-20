def positive(some_num):
    return [num for num in some_num if int(num) >= 0]


def nega(some_num):
    return [num for num in some_num if int(num) < 0]


numbers = input().split(', ')
numbers_int = [int(num) for num in numbers]

# positive = []
neg = []
even = []
odd = []
for num in numbers_int:

    # if num >= 0:
    #     positive.append(str(num))
    # else:
    #     neg.append(str(num))

    if num % 2 == 0:
        even.append(str(num))
    else:
        odd.append(str(num))

print(f'Positive: {", ".join(positive(numbers))}')
print(f'Negative: {", ".join(nega(numbers))}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')

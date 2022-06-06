n = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(n):
    num = int(input())
    if num >= 0:
        positive.append(num)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    elif num < 0:
        negative.append(num)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

category = input()

if category == "even":
    print(even)
elif category == "odd":
    print(odd)
elif category == "negative":
    print(negative)
elif category == "positive":
    print(positive)
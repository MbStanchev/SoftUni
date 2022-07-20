enrty = input().split()
total_sum = 0
first = enrty[0]
second = enrty[1]
counter = 0

if len(first) == len(second):
    for index in range(len(first)):
        result = ord(first[index]) * ord(second[index])
        total_sum += result
elif len(first) > len(second):
    for index in range(len(second)):
        result = ord(first[index]) * ord(second[index])
        total_sum += result
    for index in range(len(second), len(first)):
        total_sum += ord(first[index])
elif len(second) > len(first):
    for index in range(len(first)):
        result = ord(first[index]) * ord(second[index])
        total_sum += result
    for index in range(len(first), len(second)):
        total_sum += ord(second[index])

print(total_sum)

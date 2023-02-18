from collections import deque

entry = [int(x) for x in input().split(", ")]
serched_indx = int(input())
result = deque()
for indx in range(len(entry)):
    result.append((entry[indx], indx))
aha = 0
result = sorted(result)
for val, indx in result:
    aha += val
    if indx == serched_indx:
        break
print(aha)
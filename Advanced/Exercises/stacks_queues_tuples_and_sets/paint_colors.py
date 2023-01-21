from collections import deque

strings = deque(input().split())
main = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]
result = []
while strings:
    if len(strings) > 1:
        first = strings.popleft()
        second = strings.pop()
        test = first + second
        test2 = second + first
        if test in main or test in secondary:
            result.append(test)
        elif test2 in main or test2 in secondary:
            result.append(test2)
        else:
            first = first[:-1]
            if len(first) > 0:
                strings.insert(len(strings)//2, first)
            second = second[:-1]
            if len(second) > 0:
                strings.insert(len(strings)//2, second)
    elif len(strings) == 1:
        just_one = strings.popleft()
        if just_one in main or just_one in secondary:
            result.append(just_one)

for el in result:
    if el in secondary:
        if el == "orange":
            pass
        elif el == "purple":
            if 'blue' not in result:
                pass
            else:
                result.remove("purple")
        elif el == "green":
            pass
print(result)
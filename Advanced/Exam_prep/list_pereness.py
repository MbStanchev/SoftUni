from collections import deque


def best_list_pureness(el: list, numb_rotat: int):
    results = {}
    numbs = deque(el)
    for indx in range(numb_rotat + 1):
        if indx == len(numbs):
            break
        result = sum([k*v for k, v in enumerate(numbs)])
        numbs.appendleft(numbs.pop())
        results.update({indx: result})

    max_val = max(results.values())
    for k, v in results.items():
        if v == max_val:
            return f"Best pureness {max_val} after {k} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


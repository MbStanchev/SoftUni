sequence = [int(x) for x in input().split()]
capacity_rack = int(input())
rack = 1
current_capacity = 0
while sequence:
    if current_capacity + sequence[-1] > capacity_rack:
        rack += 1
        current_capacity = 0
    else:
        clouthing = sequence.pop()
        current_capacity += clouthing
print(rack)

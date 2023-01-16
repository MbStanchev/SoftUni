def range_of(entry):
    start, end = [int(x) for x in entry.split(',')]
    return set(range(start, end + 1))


n = int(input())
the_best = set()
for i in range(n):

    line = input().split('-')

    # first_iner = [int(x) for x in line[0].split(',')]
    # start = first_iner[0]
    # end = first_iner[1]
    one = range_of(line[1])

    # second_iner = [int(y) for y in line[1].split(',')]
    # start2 = second_iner[0]
    # end2 = second_iner[1]
    two = range_of(line[0])

    longest = one.intersection(two)
    if len(longest) > len(the_best):
        the_best = longest
print(f'Longest intersection is [{", ".join(str(x) for x in the_best)}] with length {len(the_best)}')
def diference(a,b):
    ab = a - b
    return ab


def max_count_per_shell(n):
    result = 2 * n ** 2
    return result


number_of_electrons = int(input())
sum_all_electrons = 0
output = []
# 3rd shield can be 2*32 = 18

for num_of_shells in range(1, number_of_electrons + 1):
    diff = diference(number_of_electrons, sum_all_electrons)
    max_count_electrons = max_count_per_shell(num_of_shells)
    if diff == 0:
        break
    if max_count_electrons <= diff:
        output.append(max_count_electrons)
        sum_all_electrons += max_count_electrons
    else:
        output.append(diff)
        break
print(output)


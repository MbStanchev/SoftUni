num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_f(a, b):
    result_1 = a + b
    return result_1


def substrat(sum, c):
    result_2 = sum - c
    return result_2


def add_and_subtract(f, s, t):
    sum_of_f = sum_f(num_1, num_2)
    result = substrat(sum_of_f, t)
    return result


print(add_and_subtract(num_1,num_2,num_3))
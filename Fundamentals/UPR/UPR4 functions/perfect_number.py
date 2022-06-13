num = int(input())

lis_of_deviders = []



def is_num_perfect(some_number):
    is_perfect = True
    for i in range(1 ,num):
        if num % i == 0:
            lis_of_deviders.append(i)
    sum_of_list = sum(lis_of_deviders)
    if sum_of_list != num:
        is_perfect = False
    return is_perfect


if is_num_perfect(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
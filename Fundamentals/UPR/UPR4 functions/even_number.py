number = list(map(int, input().split( )))
even = []
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even,number))
# print(result)


def even_num(num):
    if num % 2 == 0:
        return True


for i in number:
    if even_num(i):
        resul = list(filter(even_num,number))
        even.append(i)
print(even)
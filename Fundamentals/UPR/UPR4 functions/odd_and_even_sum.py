initial_number = input()
list = []
odd_sum = 0
even_sum = 0

for i in initial_number:
    list.append(i)
odd = []
even = []

def odd_and_even(some_num):
    if some_num % 2 == 0:
        return True


for num in list:
    if odd_and_even(int(num)):
        even_sum += (int(num))
    else:
        odd_sum += (int(num))

# for odd_num in odd:
#     odd_sum += odd_num
#
# for even_num in even:
#     even_sum += even_num

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


# def odd_even_sum(number: int):
#     even_sum = 0
#     odd_sum = 0
#     num_to_str = str(number)
#     for element in num_to_str:
#         if int(element) % 2 == 0:
#             even_sum += int(element)
#         else:
#             odd_sum += int(element)
#     return f"Odd sum = {odd_sum}, Even sum = {even_sum}"
#
#
# digit = int(input())
# print(odd_even_sum(digit))
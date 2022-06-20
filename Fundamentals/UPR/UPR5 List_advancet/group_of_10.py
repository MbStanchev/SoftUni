# sequence_of_numbers = input().split(", ")
# sequence = sequence_of_numbers.copy()
#
# g_10 = []
# g_20 = []
# g_30 = []
# g_40 = []
# g_50 = []
#
# max_num = 0
#
# while len(sequence_of_numbers) != 0:
#
#     for number in sequence_of_numbers.copy():
#         if int(number) > max_num:
#             max_num = int(number)
#
#         if 0 < int(number) <= 10:
#             g_10.append(int(number))
#             sequence_of_numbers.remove(number)
#
#         elif 10 < int(number) <= 20:
#             g_20.append(int(number))
#             sequence_of_numbers.remove(number)
#
#         elif 20 < int(number) <= 30:
#             g_30.append(int(number))
#             sequence_of_numbers.remove(number)
#
#         elif 30 < int(number) <= 40:
#             g_40.append(int(number))
#             sequence_of_numbers.remove(number)
#
#         elif 40 < int(number) <= 50:
#             g_50.append(int(number))
#             sequence_of_numbers.remove(number)
# if max_num <= 10:
#     print(f"Group of 10's: {g_10}")
# elif max_num <= 20:
#     print(f"Group of 10's: {g_10}")
#     print(f"Group of 20's: {g_20}")
# elif max_num <= 30:
#     print(f"Group of 10's: {g_10}")
#     print(f"Group of 20's: {g_20}")
#     print(f"Group of 30's: {g_30}")
# elif max_num <= 40:
#     print(f"Group of 10's: {g_10}")
#     print(f"Group of 20's: {g_20}")
#     print(f"Group of 30's: {g_30}")
#     print(f"Group of 40's: {g_40}")
# elif max_num <= 50:
#     print(f"Group of 10's: {g_10}")
#     print(f"Group of 20's: {g_20}")
#     print(f"Group of 30's: {g_30}")
#     print(f"Group of 40's: {g_40}")
#     print(f"Group of 50's: {g_50}")

import math

sequence_of_numbers = input().split(", ")
sequence = sequence_of_numbers.copy()
int_siq = [int(num) for num in sequence_of_numbers.copy()]
max_num = max(int_siq)
limit = 10
while len(sequence_of_numbers) != 0:
    lis = []
    num = 0
    for num in sequence_of_numbers.copy():
        if int(num) <= limit:
            lis.append(int(num))
            sequence_of_numbers.remove(str(num))
    print(f"Group of {limit}'s: {lis}")
    limit += 10
import math

budget = float(input())
students = int(input())
price_flower = float(input())
price_eggs = float(input())
price_apron = float(input())
# flower_counter = 0
# eggs_counter = 0
# apron_counter = 0
# for i in range(students):
#     eggs_counter += 10
#     apron_counter += 1 * 1.2
free_flover = students // 5
cost = price_apron*(math.ceil(students * 1.2)) + (price_eggs * students * 10) + price_flower * (students - free_flover)
diff = cost-budget
if budget >= cost:
    print(f'Items purchased for {cost:.2f}$.')
else:
    print(f'{diff:.2f}$ more needed.')
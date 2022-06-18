

happines_as_string = input().split()
happines_as_digits = [int(num) for num in happines_as_string]
factor = int(input())
happy_count = 0
total_count = len(happines_as_digits)

employees_happines = list(map(lambda x: x * factor, happines_as_digits))
avarege_happines = sum(employees_happines) / len(employees_happines)
for i in employees_happines:
    if i >= avarege_happines:
        happy_count += 1

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
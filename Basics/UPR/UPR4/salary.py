num_open_tabs = int(input())
salary = int(input())

for i in range (num_open_tabs):
    if salary <=0:
        break
    name_of_site = input()
    if name_of_site == "Facebook":
        salary -= 150
    elif name_of_site == "Instagram":
        salary -= 100
    elif name_of_site == "Reddit":
        salary -= 50

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(salary)


day_of_week = input()
price = 0

is_1 = day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday"
is_2 = day_of_week == "Wednesday" or day_of_week == "Thursday"
is_3 = day_of_week == "Saturday" or day_of_week == "Sunday"

if is_1:
    price = 12

elif is_2:
    price = 14

elif is_3:
    price = 16

print(price)


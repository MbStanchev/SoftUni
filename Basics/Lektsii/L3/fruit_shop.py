fruit = input()
day_of_week = input()
quantity = float(input())

price = 0

is_type_fruit = fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes"
work_days = day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday"
weekends = day_of_week == "Saturday" or day_of_week == "Sunday"

if is_type_fruit:
    if work_days:
        if fruit == "banana":
            price = 2.5
        elif fruit == "apple":
            price = 1.2
        elif fruit == "orange":
            price = 0.85
        elif fruit == "grapefruit":
            price = 1.45
        elif fruit == "kiwi":
            price = 2.70
        elif fruit == "pineapple":
            price = 5.5
        elif fruit == "grapes":
            price = 3.85

    elif weekends:
        if fruit == "banana":
            price = 2.7
        elif fruit == "apple":
            price = 1.25
        elif fruit == "orange":
            price = 0.90
        elif fruit == "grapefruit":
            price = 1.60
        elif fruit == "kiwi":
            price = 3
        elif fruit == "pineapple":
            price = 5.6
        elif fruit == "grapes":
            price = 4.2


total_price = price * quantity
if price == 0:
    print("error")
else:
    print(f"{total_price:.2f}")




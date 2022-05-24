hour = float(input())
day_of_week = input()

is_workday = day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday"
is_dayoff = day_of_week == "Sunday"

if is_workday:
    if hour >= 10 and hour <= 18:
        print("open")
    else:
        print("closed")
elif is_dayoff:
    print("closed")
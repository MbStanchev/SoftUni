day_of_the_week = input()

is_working_day = day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" or day_of_the_week == "Friday"
is_weekend = day_of_the_week == "Saturday" or day_of_the_week == "Sunday"

if is_working_day:
    print("Working day")
elif is_weekend:
    print("Weekend")
else:
    print("Error")

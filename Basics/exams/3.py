days_of_stay = int(input())
room_type = input()
grade = input()
cost_for_stay = 0
nights = days_of_stay - 1

if room_type == "room for one person":
    cost_for_stay = nights * 18
elif room_type == "apartment":
    if days_of_stay < 10:
        cost_for_stay = (nights * 25) * 0.7
    elif 10 <= days_of_stay <=15:
        cost_for_stay = (nights * 25) * 0.65
    else:
        cost_for_stay = (nights * 25) * 0.5
elif room_type == "president apartment":
    if days_of_stay < 10:
        cost_for_stay = (nights * 35) * 0.9
    elif 10 <= days_of_stay <=15:
        cost_for_stay = (nights * 35) * 0.85
    else:
        cost_for_stay = (nights * 35) * 0.80

if grade == "positive":
    all_cost = cost_for_stay * 1.25
else:
    all_cost = cost_for_stay * 0.9

print(f"{all_cost:.2f}")
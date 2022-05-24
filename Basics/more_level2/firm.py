import math

neede_hurs = int(input())
day_for_project = int(input())
num_of_emploies_overtame = int(input())

working_time = day_for_project * 8 * 0.9
overtime = day_for_project * 2 * num_of_emploies_overtame
all_work_hours = math.floor(working_time + overtime)

difference = abs(neede_hurs - all_work_hours)
if all_work_hours >= neede_hurs:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")
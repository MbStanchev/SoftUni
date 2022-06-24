num_of_students = int(input())
all_lectures = int(input())
additional_bonus = int(input())
max_student_attendances = 0
bonus_points_per_student = 0
all_bous = []

for i in range(num_of_students):
    student_attendances = int(input())
    if student_attendances > max_student_attendances:
        max_student_attendances = student_attendances
    bonus_points_per_student = (student_attendances / all_lectures * (5 + additional_bonus))
    all_bous.append(round(bonus_points_per_student))
max_points = max(all_bous)

print(f'Max Bonus: {max_points}.')
print(f'The student has attended {max_student_attendances} lectures.')

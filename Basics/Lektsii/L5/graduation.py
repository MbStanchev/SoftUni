name_of_student = input()

years_couter = 1
avarege = 0
sum = 0
rep = 0
gradueited = True
while years_couter <= 12:
    if rep > 1:
        gradueited = False
        break
    grade = float(input())

    if grade >= 4:
        years_couter += 1
        sum += grade
        avarege = sum / 12
    else:
        rep += 1

if gradueited:
    print(f"{name_of_student} graduated. Average grade: {avarege:.2f}")
else:
    print(f"{name_of_student} has been excluded at {years_couter} grade")
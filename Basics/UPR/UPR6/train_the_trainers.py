num_of_jurey = int(input())
presentation = input()
presentation_couner = 0
all_average_grade = 0

while presentation != "Finish":
    average_grade = 0
    sum_grade = 0
    for i in range(num_of_jurey):
        grade = float(input())
        sum_grade += grade
    average_grade = sum_grade / num_of_jurey
    all_average_grade += average_grade
    presentation_couner += 1

    print(f"{presentation} - {average_grade:.2f}.")

    presentation = input()
averagr_grade_all_presantetion = all_average_grade / presentation_couner
print(f"Student's final assessment is {averagr_grade_all_presantetion:.2f}.")

# "{името на презентацията} - {средна оценка}."
# "Student's final assessment is {среден успех от всички презентации}."

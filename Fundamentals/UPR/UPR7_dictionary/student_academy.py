num_of_students = int(input())
di = {}
for students in range(num_of_students):

    student_name = input()
    grade = float(input())

    if student_name not in di:
        di[student_name]=[]
    di[student_name].append(grade)
aaaa = {}
for sudent, grade in di.items():
    avarage = sum(grade)/len(grade)
    if avarage >= 4.5:
        aaaa[sudent]=avarage

for student_name,avarage in aaaa.items():
    print(f"{student_name} -> {avarage:.2f}")
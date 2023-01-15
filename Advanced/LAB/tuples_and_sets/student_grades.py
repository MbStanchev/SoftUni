students = int(input())
record = {}
for _ in range(students):
    names, grades = (input().split())
    if names not in record:
        record[names] = []
    record[names].append(float(grades))
for student in record.items():
    print(f"{student[0]} -> {' '.join([f'{el:.2f}' for el in student[1]])} (avg: {sum(student[1]) / len(student[1]):.2f})")

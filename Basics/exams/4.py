num_of_students = int(input())
fail = 0
week = 0
good = 0
exelet =0
sum = 0
for i in range(num_of_students):
    grade = float(input())
    if grade < 3:
        fail += 1
        sum += grade
    elif 3 <= grade < 4:
        week += 1
        sum += grade
    elif 4 <= grade < 5:
        good += 1
        sum += grade
    elif grade >= 5:
        exelet += 1
        sum += grade
average = sum / num_of_students
fail_posent = fail / num_of_students * 100
week_posent = week / num_of_students * 100
good_posent = good / num_of_students * 100
exelent_posent = exelet / num_of_students * 100

print(f"Top students: {exelent_posent:.2f}%")
print(f"Between 4.00 and 4.99: {good_posent:.2f}%")
print(f"Between 3.00 and 3.99: {week_posent:.2f}%")
print(f"Fail: {fail_posent:.2f}%")
print(f"Average: {average:.2f}")
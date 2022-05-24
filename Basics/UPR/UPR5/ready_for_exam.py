num_faild_grades = int(input())
name_of_task = input()
all_grades = 0
average_score = 0
fail_counter = 0
task_counter = 0
last_task = ""
faild = False
while name_of_task != "Enough":

    grade = int(input())

    all_grades += grade
    if grade <= 4:
        fail_counter += 1

    task_counter += 1
    average_score = all_grades / task_counter
    last_task = name_of_task
    if fail_counter == num_faild_grades:
        faild = True
        break
    name_of_task = input()
if faild == False:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {task_counter}")
    print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {fail_counter} poor grades.")
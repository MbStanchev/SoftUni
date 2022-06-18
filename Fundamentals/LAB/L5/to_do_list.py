to_do_notes = input().split("-")
lst = []


while to_do_notes[0] != "End":
    index = int(to_do_notes[0])
    task = to_do_notes[1]
    lst.append((index, task))


    to_do_notes = input().split("-")

sorted_tasks = [task_data[1] for task_data in sorted(lst)]

print(sorted_tasks)

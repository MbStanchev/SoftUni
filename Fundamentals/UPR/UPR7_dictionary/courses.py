entry = input().split(' : ')
di = {}
while entry[0] != 'end':
    name = entry[1]
    course = entry[0]

    if course not in di:
        di[course] = []
    di[course].append(name)
    entry = input ().split (' : ')

for cousres, students in di.items():
    print(f"{cousres}: {len(students)}")
    for name_of_sudent in students:
        print(f"-- {''.join(name_of_sudent)}")
# sorted_= sorted(di.items(),key=)
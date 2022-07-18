command = input()
exam = {}
banned = []
language = {}
while command != "exam finished":
    split_baned = command.split('-')
    if split_baned[1] == 'banned':
        # user = split_baned[0]
        # del exam[user]
        banned.append(command.split('-')[0])
        command = input()
        continue

    entry = command.split('-')
    username = entry[0]
    lang = entry[1]
    points = int(entry[2])

    if username not in exam:
        exam[username] = 0
        if exam[username] < points:
            exam[username] = points
    else:
        exam[username] = points

    if lang not in language:
        language[lang] = 0
    language[lang] += 1
    command = input()

for items in range(0, len(banned)):
    if banned[items] in exam:
        exam.pop(banned[items])

print('Results:')
for k, v in exam.items():
    print(f'{k} | {v}')
print('Submissions:')
for lang_type, lang_count in language.items():
    print(f'{lang_type} - {lang_count}')

# sortet_exam = sorted(exam.items(), key=lambda kvtp: (-kvtp[1], kvtp[0]))

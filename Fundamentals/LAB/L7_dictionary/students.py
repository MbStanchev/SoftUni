entry = input()
di = {}
while ':' in entry:
    name, id, courses = entry.split(':')
    if courses not in di:
        di[courses]= {}
    di[courses][name] = int(id)
    entry = input()

if '_' in entry:
    entry = entry.replace('_', ' ')

for k, v in di[entry].items():
    print(f'{k} - {v}')
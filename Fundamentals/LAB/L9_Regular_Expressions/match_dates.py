import re
data = input()
# pattern = r'\b\d{2}([-\./])[A-Z][a-z]{2}\1\d{4}\b'
# mached_dates = re.finditer(pattern,data)
# mached_dates = [matched.group(0) for matched in mached_dates]
# for i in mached_dates:
#     print(f'Day: {i[0:2]}, Month: {i[3:6]}, Year: {i[7:11]}')

pattern = r'(?P<day>\d{2})(?P<separator>[-\./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})'
matched_dates = re.finditer(pattern, data)
for i in matched_dates:
    d = i.groupdict()
    print(f'Day: {d["day"]}, Month: {d["month"]}, Year: {d["year"]}')
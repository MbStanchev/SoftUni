import re

pattern = r'(#|\|)(?P<name>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<cal>\d+)\1'
data = input()
items = []
cal = 0
my_dick = {}
matches = re.finditer(pattern,data)
# match = re.findall(pattern,data)
# for i in match:
#    items.append(i[1])
#    cal += int(i[3])
# day_to_last = cal//2000
#
# print(f'You have food to last you for: {day_to_last} days!')
# for food in match:
#     print(f'Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}')
for match in matches:
    result = match.groupdict()
    cal += int(match["cal"])
    items.append(result)
day_to_last = cal//2000

print(f'You have food to last you for: {day_to_last} days!')
for food in items:
    print(f'Item: {food["name"]}, Best before: {food["date"]}, Nutrition: {food["cal"]}')

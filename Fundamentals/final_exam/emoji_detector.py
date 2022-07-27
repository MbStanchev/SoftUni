import re
command = input()
counter = 0
lst = []
redy_lst = []
pattern = r'(\:{2}[A-Z][a-z]{2,}\:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})'
matches = re.finditer(pattern, command)
pattern_2 = r'\d'
matches_2 = re.findall(pattern_2, command)
threshold = 1
for i in matches_2:
    threshold *= int(i)
for res in matches:
    counter += 1
    word = res.group()
    result = 0
    for ch in word:
        if ch != ':' and ch != '*':
            result += ord(ch)
    if result > threshold:
        redy_lst.append(word)
print(f'Cool threshold: {threshold}')
print(f'{counter} emojis found in the text. The cool ones are:')
for some in redy_lst:
    print(some)



























# int_i = [int(i) for i in matches_2]
# threshold = 1
# for num in range(len(matches_2)):
#     threshold *= int(matches_2[num])
# print(f'Cool threshold: {threshold}')
# print(f'{int(len(matches[2])+1)} emojis found in the text.')
# print('The cool ones are:')
# for i in matches:
#     word = i[2]
#     total = 0
#     for ch in word:
#         counter += 1
#         total += ord(ch)
#         if total > threshold:
#             print(f'{i[1]}{i[2]}{i[1]}')
#             break
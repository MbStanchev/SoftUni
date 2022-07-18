word = input()
str_to_check = input()
result = ''
while word in str_to_check:
    str_to_check = str_to_check.replace(word, '')
print(str_to_check)
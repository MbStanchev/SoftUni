simb = ["-", ",", ".", "!", "?"]

with open('../../../files/text.txt', 'r') as even_lines_file:
    f = even_lines_file.readlines()

print(f)

for row in range(0, len(f), 2):
    for sybol in simb:
        f[row] = f[row].replace(sybol, '@')
    print(f)
# file = open("files/text.txt", "r")
# t = file.read()
# print(t)
#a = input()
#b = input()
#c = input()

#import string
#for i in string.ascii_lowercase:
    #print(i, end=" ")

def character_range(char1, char2):
    char1 = input()
    char2 = input()

    for char in range(ord(char1), ord(char2) + 1):
        yield (char)



char3 = input()
for letter in character_range('a', 'z'):
    if chr(letter) == char3:
        break
    print(chr(letter), end=' ')

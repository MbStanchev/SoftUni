char_1 = input()
char_2 = input()

def chars_from_ascii(a,b):
    list=[]
    for i in range(ord(a)+1,ord(b)):
        list.append(chr(i))
    return list


print(" ".join(chars_from_ascii(char_1,char_2)))
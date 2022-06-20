secret_message = input().split()
desifered_message = []
for this_word in secret_message:
    number = ""
    letter = ""
    curent = ""
    for num in this_word:
        if num.isdigit():
            number += num
        else:
            letter += num
    if len(letter) >= 2:
        letter = letter [-1] + letter [1:-1] + letter[0]
    curent += (chr(int(number))) + letter
    desifered_message.append(curent)
print(" ".join(desifered_message))

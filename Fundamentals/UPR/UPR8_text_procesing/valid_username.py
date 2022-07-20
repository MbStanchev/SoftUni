usernames = input().split(', ')
result = ''
for word in usernames:
    if 3 <= len(word) <= 13:
        if word.isalnum() or '_' in word or '-' in word:
            pass
            result += word
            print(word)
            word = ''
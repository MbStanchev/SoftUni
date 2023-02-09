def palindrome(word, inx):
    if inx == len(word)//2:
        return f'{word} is a palindrome'

    if word[inx] != word[-1 - inx]:
        return f'{word} is not a palindrome'
    return palindrome(word, inx + 1)


print(palindrome("abcba", 0))



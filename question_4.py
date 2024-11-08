def isPalindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    else:
        return False

print(isPalindrome("brb"))
print(isPalindrome("soran"))

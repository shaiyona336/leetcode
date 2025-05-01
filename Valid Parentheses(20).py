def isValid(S):
    isOpenBracket = []
    isValid = ['[', ']', '{', '}', '(', ')']
    matchingOpenBracket = {']': '[', '}': '{', ')': '('}

    for char in s:
        if char not in isValid:
            return False
        if char in matchingOpenBracket:
            if len(isOpenBracket) == 0 or matchingOpenBracket[char] != isOpenBracket[len(isOpenBracket)-1]:
                return False
            del isOpenBracket[-1]
        else:
            isOpenBracket.append(char)
        if len(isOpenBracket) > 0:
            return False
    return True

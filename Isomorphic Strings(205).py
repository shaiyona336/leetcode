def isIsomorphic(s,t):
    mapLatters = {}
    currIndex = 0
    size = len(s)

    if len(s) != len(t):
        return False

    while currIndex < size:
        currLatter = s[currIndex]
        if currLatter in mapLatters:
            if mapLatters[currLatter] != t[currIndex]:
                return False
        else:
            if t[currIndex] in mapLatters.values():
                return False
            mapLatters[currLatter] = t[currIndex]
        currIndex += 1

    return True

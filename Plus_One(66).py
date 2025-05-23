def PlusOne(digits):
    currIndex = len(digits)-1
    while True:
        if currIndex < 0:
            digits = [1] + digits
            currIndex -= 1
        elif digits[currIndex] == 9:
            digits[currIndex] = 0
            currIndex -= 1
        else:
            digits[currIndex] += 1
            return digits

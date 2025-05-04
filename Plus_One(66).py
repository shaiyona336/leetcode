def PlusOne(digits):
    currIndex = len(digits)-1
    while True:
        if currIndex < 0:
            digits = [1] + digits
        elif digits[currIndex] == 9:
            digits[currIndex] = 0
        else:
            digits[currIndex] += 1
            return digits

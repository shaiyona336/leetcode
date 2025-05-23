class Solution:
 def romanToInt(self, s: str) -> int:
    romanToValue = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    }
    size = len(s)
    if size == 0:
        return 0
    currSum = 0
    for currIndex in range (size-1):
        if romanToValue[s[currIndex]] < romanToValue[s[currIndex+1]]:
            currSum -= romanToValue[s[currIndex]]
        else:
            currSum += romanToValue[s[currIndex]]

    return currSum+romanToValue[s[size-1]]
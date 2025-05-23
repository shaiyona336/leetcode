class Solution:
    def makeSeriesWithNewDigit(self, serial, newDigit, digitToLatter):
        toReturn = []
        for digit in digitToLatter[newDigit]:
            toReturn.append(serial + digit)
        return toReturn


    def letterCombinations(self, digits: str):
        toReturn = []
        digitToLatters = digitToLatters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
        for digit in digits:
            if toReturn == []:
                for latter in digitToLatters[digit]:
                    toReturn.append(latter)
            else:
                newReturn = []
                for serial in toReturn:
                    replace = self.makeSeriesWithNewDigit(serial,digit,digitToLatters)
                    for newSerial in replace:
                        newReturn.append(newSerial)
                toReturn = newReturn
        
        return toReturn





# Test case
if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    result = solution.letterCombinations(digits)
    print(result)  # Expected output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
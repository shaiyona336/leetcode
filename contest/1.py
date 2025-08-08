class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        index = len(number)-1

        while index >=0:
          if digit[index] == digit:
            number = number[:index] + number[index+1:]
            return number
          index -= 1

        return number

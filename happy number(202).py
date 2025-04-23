class Solution(object):
    def squareDigits(self, n):
        nInString = str(n)
        numberToReturn = 0

        for digit in nInString:
            numberToReturn += int(digit)**2
        
        return numberToReturn

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numberAlreadyBeen = set()

        while (True):
            n = self.squareDigits(n)
            if (n == 1):
                return True
            if (n in numberAlreadyBeen):
                return False
            numberAlreadyBeen.add(n)
            


solution = Solution()
print(solution.isHappy(19)) # Expected output: True
class Solution:
    def soupServings(self, n: int) -> float:
        self.saveSolutions = {}
        if n > 5000:
            return 1
        return self.helper(n,n)


    def helper(self, firstCup, secondCup):
        if (firstCup,secondCup) in self.saveSolutions:
            return self.saveSolutions[(firstCup,secondCup)]
        #base cases
        if (firstCup <= 0 and secondCup <= 0):
            return 0.5
        if (firstCup <= 0):
            return 1
        if (secondCup <= 0):
            return 0 
        #recursion
        sumProbabilty = 0.25*self.helper(firstCup-100,secondCup)
        sumProbabilty += 0.25*self.helper(firstCup-75,secondCup-25)
        sumProbabilty += 0.25*self.helper(firstCup-50,secondCup-50)
        sumProbabilty += 0.25*self.helper(firstCup-25,secondCup-75)
        self.saveSolutions[(firstCup,secondCup)] = sumProbabilty
        return sumProbabilty



    
n = 100
probability = 0
solution = Solution()


while probability < 1 - 10^(-5):
    probabilty = solution.soupServings(n)
    n += 1

print(n)

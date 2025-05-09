import math
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        countBalance = 0
        num = str(num)
        sumDigits = sum(int(digit) for digit in num)
        solutions = set()

        if sumDigits % 2 == 1:
            return 0

        digitInNum = {}
        for digit in num:
            self.addNumToSet(digitInNum,digit)

        self.helper(num,digitInNum,sumDigits/2,math.floor(len(num)/2)+1,0,0)
        for solution in solutions:
            numPermutations = math.factorial(len(solution)) #num way for even indexes
            numPermuatations += math.factorial(len(num)-len(solution))
            countBalanace += numPermutations
        
        return countBalance

    
    def helper(self,num,digitInNum,targetSum, targetCount, currSum,currCount):#check if can get to target with 
        if currSum > targetSum or currCount > targetCount:
            return

        if currSum == targetSum and currCount == targetCount:
            numsInSolution = []
            for digit in digitInNum:
                for i in range(digitInNum[digit]):
                    numsInSolution.append(digit)
            solution.add(sorted(numsInSolution))

        for i in range(len(num)-len(digitInNum)):
            self.addNumToSet(digitInNum,num[i])
            currCount += 1
            currSum += int(num[i])
            self.helper(num,digitInNum,targetSum,targetCount,currSum,currCount)
            currSum -= int(num[i])
            currCount -= 1
            digitInNum[num[i]] -= 1



    def addNumToSet(self,array,value):
        if value in array:
            array[value] += 1
        else:
            array[value] = 1



        
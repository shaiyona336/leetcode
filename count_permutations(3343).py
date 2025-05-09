import math
def CountBalancedPermutations(num):
    num = str(num)
    sumDigits = sum(int(digit) for digit in num))
    solutions = set()

    if sumDigits % 2 == 1:
        return 0

    digitInNum = {}
    for digit in num:
        addNumToSet(digitInNum,digit)

    helper(num,digitInNum,sumDigits/2,math.floor(len(num)/2)+1,0,0)

    
def helper(num,digitInNum,targetSum, targetCount, currSum,currCount):#check if can get to target with 
    if currSum > targetSum or currCount > targetCount:
        return

    if currSum == targetSum and currCount == targetCount:
        solution.add(digitInNum)

    for i in range(len(n)-len(digitInNum)):
        addNumToSet(digitInNum,num[i])
        currCount += 1
        currSum += num[i]
        helper(num,digitInNum,targetSum,targetCount,currSum,currCount)
        currSum -= num[i]
        currCount -= 1
        digitInNum[num[i] -= 1



addNumToSet(array,value):
    if value in array:
        array[value] += 1
    else:
        array[value] = 1



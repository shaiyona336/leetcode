class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        maxSum = 0
        currSum = 0
        left = 0

        for right in range(len(fruits)):
            leftPos = fruits[left][0]
            rightPos = fruits[right][0]
            currSum += fruits[right][1]

            while left<=right:
                leftPos=fruits[left][0]
                stepsRequire = rightPos-leftPos+min(abs(startPos-leftPos),abs(startPos-rightPos))

                if stepsRequire<=k:
                    break
                currSum-=fruits[left][1]
                left+=1
                

            maxSum = max(maxSum,currSum)

        return maxSum

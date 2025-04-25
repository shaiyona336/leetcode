class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        arrayToReturn = []
        nums = sorted(nums)

        currLeftIndex = 0
        currRightIndex = 0

        while (currRightIndex < len(nums)):
            if (nums[currRightIndex] == nums[currLeftIndex] + currRightIndex):
                currRightIndex += 1
            else:
                currRightIndex -= 1 if currRightIndex > currLeftIndex else 0
                if (currLeftIndex == currRightIndex):
                    arrayToReturn.append(str(nums[currLeftIndex]))
                else:
                    arrayToReturn.append(str(nums[currLeftIndex]) + "->" + str(nums[currRightIndex]))
                currRightIndex += 1
                currLeftIndex = currRightIndex        

        if (currLeftIndex == currRightIndex-1):
                arrayToReturn.append(str(nums[currLeftIndex]))
        else:
            arrayToReturn.append(str(nums[currLeftIndex-1]) + "->" + str(nums[currRightIndex-1]))

        return arrayToReturn
        

solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7])) # Expected output: ["0->2","4->5","7"]
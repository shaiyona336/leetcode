class Solution:
    def minSubArrayLen(self, target, nums):
        bestCount = float('inf')
        sum = 0
        currCount = 0
        currUsedIndexes = []

        if len(nums) == 0:
            return 0

        for index in range(len(nums)):       
            sum += nums[index]
            currCount += 1
            currUsedIndexes.append(index)
            while sum >= target:
                bestCount = min(currCount,bestCount)
                sum -= nums[currUsedIndexes[0]]
                currCount -= 1
                currUsedIndexes = currUsedIndexes[1:]

        if bestCount == float('inf'):
            return 0
        return bestCount


        
        

# Example usage:
solution = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(solution.minSubArrayLen(target, nums))  # Output: 2 (subarray [4,3] has the minimal length under the problem constraint)
import copy
class Solution:
    def check_all_zeroes(self,nums) -> int:
        for num in nums:
            if num != 0:
                return False
        return True


    def minOperations(self, nums) -> int:
        return self.helper(nums,nums)
    
    
    def helper(self, nums, allArray) -> int:
        if self.check_all_zeroes(allArray):
            return 0
        minCount = float('inf')
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                currCount = 0
                subarray = copy.deepcopy(nums[i:j])
                minValue = min(subarray)
                for k in range(i,j):
                    if nums[k] == minValue:
                        nums[k] = 0
                currCount += 1 + self.helper(nums[:i]+nums[j+1:],allArray)
                minCount = min(minCount,currCount)

        return minCount

    

solution = Solution()

nums = [3,1,2,1]
print(solution.minOperations(nums))  # Output: 1
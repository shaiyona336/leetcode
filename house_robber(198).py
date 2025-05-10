class Solution:
    def rob(self, nums: List[int]) -> int:
        maxUntilIWith = [0]*len(nums)
        maxUntilIWithout = [0]*len(nums)
        if len(nums) == 0:
            return
        maxUntilIWith[0] = nums[0]
        for i in range(1,len(nums)):
            maxUntilIWithout[i] = maxUntilIWith[i-1]
            maxUntilIWith[i] = max(maxUntilIWith[i-1],maxUntilIWithout[i-1]+nums[i])
            
        return maxUntilIWith[len(nums)-1]
        

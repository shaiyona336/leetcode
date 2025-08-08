class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.maxBinary = 0
        self.count = 0 
        self.size = len(nums)

        for num in nums:
            self.maxBinary |= num

        self.helper(nums, 0, 0)

        return self.count
 

    def helper(self, nums, currIndex, currNumber):
        if currIndex == self.size:
            if currNumber == self.maxBinary:
                self.count += 1
            return

        self.helper(nums, currIndex+1,currNumber|nums[currIndex])
        self.helper(nums, currIndex+1,currNumber)


                    

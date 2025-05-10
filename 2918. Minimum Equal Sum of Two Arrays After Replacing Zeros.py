class Solution:
    def countZeroes(self,nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        
        return count

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = self.countZeroes(nums1)
        count2 = self.countZeroes(nums2)
        minSum1 = sum(nums1)+count1
        minSum2 = sum(nums2)+count2
        maxSum1 = sum(nums1) if count1 == 0 else float('inf')
        maxSum2 = sum(nums2) if count2 == 0 else float('inf')

        if maxSum1 < minSum2 or maxSum2 < minSum1:
            return -1
        return max(minSum1,minSum2)
        

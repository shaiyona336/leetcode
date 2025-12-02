class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float('-inf')
        curr_sum = 0
        min_prefix = [float('inf')]*k
        min_prefix[0] = 0
        
        for i,num in enumerate(nums):
            curr_sum += num
            reminder = (i + 1) % k
            if min_prefix[reminder] != float('-inf'):
                max_sum = max(max_sum,curr_sum-min_prefix[reminder])
            min_prefix[reminder] = min(min_prefix[reminder],curr_sum)

        return max_sum if max_sum != float('-inf') else 0

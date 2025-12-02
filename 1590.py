class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        size = len(nums)
        best = size
        original_reminder = sum(nums)%p
        if original_reminder == 0:
            return 0
        curr_reminder = 0
        prefix = {0: -1}

        for index in range(len(nums)):
            curr_reminder = (curr_reminder + nums[index]) % p
            target = (curr_reminder-original_reminder)%p
            if target in prefix:
                best = min(best,index-prefix[target])
            prefix[curr_reminder] = index

        return best if best != size else -1

        
        





#need to find subarray so (sum(nums)-sum(subarray))%p=0
#can get the sum of each subarray with prefix
#example: Input: nums = [3,1,4,2], p = 6
#total sum = 10
#need to find subarray with 10 % 6 = 4 + 6k sum
#can calculate current reminder, and check for the needed reminded in
#hashmap
#needed hashmap:
#if for example p=6, and current sum = 3, we need to find
#subarray with 10-3%6=1 reminder
#needed: curr-target=original
#target = curr-original

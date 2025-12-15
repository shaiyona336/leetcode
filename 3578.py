class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        size = len(nums)
        dp = [0]*(size+1)
        prefix = [0]*(size+1)
        sliding_window = SortedList()
        dp[0]=1
        prefix[0]=1
        left = 0

        for right in range(size):
            sliding_window.add(nums[right])
            while sliding_window[-1]-sliding_window[0]>k:
                sliding_window.remove(nums[left])
                left += 1
            if left > 0:
                dp[right+1] = prefix[right]-prefix[left-1]
            else:
                dp[right+1] = prefix[right]
            prefix[right+1] = (prefix[right]+dp[right+1])%MOD

        return dp[size]

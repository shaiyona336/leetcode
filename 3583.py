class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count = 0
        left_nums = Counter()
        right_nums = Counter(nums)
        MOD = 10**9+7

        for num in nums:
            right_nums[num] -= 1
            target = num*2
            count = (count+left_nums[target]*right_nums[target])%MOD
            left_nums[num] += 1

        return count

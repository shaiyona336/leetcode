import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums,[],result)
        return result


    def helper(self, nums, nextValue, result):
        if len(nextValue) == len(nums):
            result.append(nextValue)
            return


        for num in nums:
            if num not in nextValue:
                self.helper(nums, nextValue + [num], result)



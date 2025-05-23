class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumpsToIndex = [float('inf')] * len(nums)
        minJumpsToIndex[0] = 0
        size = len(nums)

        for i in range(size):
            if minJumpsToIndex[i] == float('inf'):
                continue
            for j in range(1,nums[i]+1):
                if i+j < size:
                    if minJumpsToIndex[i+j] > minJumpsToIndex[i]+1:
                        minJumpsToIndex[i+j] = minJumpsToIndex[i]+1

        return minJumpsToIndex[size-1]

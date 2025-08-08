class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        subArrays = set()
        size = len(nums)

        for startCurrArrayIndex in range(size):
            numDivisable = 0
            currArray = []
            for j in range(startCurrArrayIndex,size):
                if nums[j] % p = 0:
                    numDivisable+=1
                if numDivisable > k:
                    break
                currArray.append(nums[j])
                subArrays.add(tuple(currArray))

        return len(subArrays)

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        
        if len(nums) == 0:
            return []

        lowestNumInGroup = nums[0]
        currGroup = 1
        index = 1
        size = len(nums)
        nums.append(0)
        arrays = []
        currArray = [nums[0]]
        while index <= size:
            if nums[index] > lowestNumInGroup+k or len(currArray) >= 3:
                lowestNumInGroup=nums[index]
                if len(currArray) < 3:
                    return []
                arrays.append(currArray)
                currArray = []
                currGroup+=1
            currArray.append(nums[index])
            index+=1

        if len(currArray) != 1:
            return []
        return arrays
                
            

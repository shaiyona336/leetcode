class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        index1 = 0
        index2 = size-1
        while index1 < index2:
            if nums[index1] == 0:
                index1 += 1
            elif nums[index2] == 2:
                index2 -= 1
            elif nums[index2] < nums[index1]:
                temp = nums[index1]
                nums[index1] = nums[index2]
                nums[index2] = temp
            elif nums[index1]==nums[index2]:
                saveIndex1 = index1
                while index1 < index2 and nums[index1] == nums[index2]:
                    index1+=1
                if nums[index1] == 0:
                    temp = nums[index1]
                    nums[index1] = nums[saveIndex1]
                    nums[saveIndex1] = temp
                    index1 = saveIndex1+1
                else:
                    temp = nums[index2]
                    nums[index2] = nums[index1]
                    nums[index1] = temp
                    index2 -= 1
                    index1 = saveIndex1
            else: #nums[index2] > nums[index1]
                index2 -= 1
        
        return nums
class Solution:
    def sortRight(self,nums,index):
        areaToFix = nums[index:len(nums)]
        areaToFix.sort()
        nums = nums[:index] + areaToFix

        return nums



    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        currIndex = size-1

        while currIndex != 0:
            if nums[currIndex] > nums[currIndex-1]:
                switchIndex = currIndex
                while switchIndex < size-1:
                    if nums[switchIndex] > nums[switchIndex+1]:
                        switchIndex+=1
                    else:
                        break
                temp = nums[currIndex-1]
                nums[currIndex-1] = nums[switchIndex]
                nums[switchIndex] = temp
                break
            currIndex -= 1
        if currIndex!=0:
            self.sortRight(nums,currIndex)
        else:
            nums.sort()
               

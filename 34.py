class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        #find left
        left = 0
        right = size - 1
        while left <= right:
            median = left + (right-left)//2
            if nums[median] >= target:
                right = median-1
            else:
                left = median+1
        foundLeft = left
        #find right
        left = 0
        right = size - 1
        while left <= right:
            median = left + (right-left)//2
            if nums[median] <= target:
                left = median+1
            else:
                right = median-1

        left = foundLeft

        if left == -1 or right == -1 or left >= size or right >= size:
            return [-1,-1]
        return [left,right] if nums[left] == target else [-1,-1]
            

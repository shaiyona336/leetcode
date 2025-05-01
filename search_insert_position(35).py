import math

def searchInsert(nums,target) -> int:
  left = middleIndex = 0
  right = len(nums) - 1

  middleIndex = math.floor((right + left) / 2)
  while left <= right:
      if nums[middleIndex] == target:
          return middleIndex
      elif target > nums[middleIndex]:
          left = middleIndex + 1
      else:
          right = middleIndex - 1
      middleIndex = math.floor((right + left) / 2)

  
  return left

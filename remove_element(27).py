def removeElement(nums, val):
  currIndex = 0
  size = len(nums)
  k = 0

  while currIndex < size - 1:
    if nums[currIndex] != val:
      k += 1
      nums[k] = nums[currIndex]
    currIndex += 1

  return k

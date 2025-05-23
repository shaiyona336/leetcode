def maxArea(height):
  left = 0
  right = len(height)-1
  maxWater = 0

  while left < right:
    currWater = min(height[left],height[right])*(right-left)
    if currWater > maxWater:
      maxWater = currWater
    if height[left] < height[right]:
      left += 1
    else:
      right -= 1

  return maxWater

print(maxArea([1,0,0,0,2,2]))

def filter(height,worthContainerIndex,currIndex):
  maxHeightAfter = max(height[index+1:]
  notWorth = []
  for containerIndex in range(len(worthContainerIndex-1)):
    for containerAfter in range(containerIndex+1,worthContainerIndex):
      if min(height[containerAfter],maxHeightAfter) > min(height[containerIndex],maxHeightAfter):
        notWorth.append(containerIndex)
        continue
    worthContainerIndex = [x for x in worthContainerIndex if x not in notWorth]
    return worthContainerIndex
    



def maxArea(height):
  if len(height) < 2:
    return 0
  maxWater = 0
  leftIndex = 0
  rightIndex = 1
  worthContainerIndex = {0} #indexes of containers that potentially can be useful for making new high with them and container from the right
  size = len(height)

  for index in range(1,size):
    for containerIndex in worthContainer:
      currWater = (min(height[containerIndex],height[index]))*(index-container)
      if currWater > maxWater:
        maxWater = currWater
      worthContainerIndex.append(index)
      worthContainerIndex = filter(worthContainerIndex,index+1)

  return maxArea


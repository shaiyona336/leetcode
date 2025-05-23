def maxArea(height):
    maxWaterk = 0
    
    if len(height) < 2:
        return 0
    leftIndex = 0
    rightIndex = 1
    leftHeight = height[0]
    rightHeight = height[1]
    maxWater = min(height[leftIndex],height[rightIndex])

    for index in range(2,len(height)):
        currHeight = height[index]
        waterWithLeft = min(leftHeight,currHeight)*(index-leftIndex)
        waterWithRight = min(rightHeight,currHeight) * (index-rightIndex)
        if waterWithLeft > maxWater or waterWithRight > maxWater:
            if waterWithLeft > waterWithRight:
                maxWater = min(leftHeight,currHeight) * (index-leftIndex)
                rightIndex = index 
            else:
                maxWater = min(rightHeight,currHeight) * (index-rightIndex) 
                temp = rightIndex
                rightIndex = index
                leftIndex = temp
        leftHeight = height[leftIndex]
        rightHeight = height[rightIndex]

    return maxWater,leftIndex,rightIndex



height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

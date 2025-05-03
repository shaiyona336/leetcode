class Solution:
    def trap(self, height):
        leftMax = 0
        rightMax = 0
        size = len(height)
        leftIndex = 0
        rightIndex = size - 1
        sumWater = 0

        while leftIndex < rightIndex:
            if height[leftIndex] < height[rightIndex]:
                if height[leftIndex] >= leftMax:
                    leftMax = height[leftIndex]
                else:
                    sumWater += leftMax - height[leftIndex]
                leftIndex += 1
            else:
                if height[rightIndex] >= rightMax:
                    rightMax = height[rightIndex]
                else:
                    sumWater += rightMax - height[rightIndex]
                rightIndex -= 1
        
        return sumWater

            
        

solution = Solution()
height = [4,3,7,0,9]
result = solution.trap(height)
print(result)
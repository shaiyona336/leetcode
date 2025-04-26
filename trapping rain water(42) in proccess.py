class Solution:
    def get_first_tile(self, height):
        indexFirstTile = 0
        size = len(height)

        while indexFirstTile < size and height[indexFirstTile] == 0:
            indexFirstTile += 1
        
        if indexFirstTile == size:
            return -1
        return indexFirstTile

    def check_if_close(self, height, index):
        currIndex = index + 1
        heightNeedToPass = height[index]
        size = len(height)

        while currIndex < size:
            if height[currIndex] >= heightNeedToPass:
                return True
            currIndex += 1
        
        return False


    def trap(self, height):
        sumWater = 0
        indexFirstTile = self.get_first_tile(height)
        size = len(height)
        isGoingToClose = False
        #if all tiles are on the ground
        if indexFirstTile == -1:
            return 0
        currTileIndex = indexFirstTile + 1
        currLeftHeight = height[indexFirstTile]
        while currTileIndex < size:
            if height[currTileIndex] >= currLeftHeight:
                indexFirstTile = currTileIndex
                while indexFirstTile < size and not isGoingToClose:
                    isGoingToClose = self.check_if_close(height,indexFirstTile)
                    if not isGoingToClose:
                        indexFirstTile += 1
                if indexFirstTile < size:
                    currLeftHeight = height[indexFirstTile]
                currTileIndex = indexFirstTile + 1
            else:
                sumWater += currLeftHeight - height[currTileIndex]
            currTileIndex += 1

        return sumWater
            
        
# Example usage:
solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = solution.trap(height)
print(result)  # Output: 6
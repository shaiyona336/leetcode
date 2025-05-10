class Solution:
    def mark_island(self,grid,marked,row,column,borderX, borderY):
        if row < 0 or column < 0 or row >= borderY or column >= borderX:
            return
        if grid[row][column] == '0' or marked[row][column]:
            return
        marked[row][column] = True
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for direction in directions:
            x,y = direction[0],direction[1]
            self.mark_island(grid,marked,row+x,column+y,borderX,borderY)


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if len(grid) == 0:
            return 0
        marked = [[False]*len(grid[0]) for row in range(len(grid))]
        for rowIndex in range(len(grid)):
            for columnIndex in range(len(grid[0])):
                if grid[rowIndex][columnIndex] == '1' and marked[rowIndex][columnIndex] == False:
                    count += 1
                    self.mark_island(grid,marked,rowIndex,columnIndex,len(grid[0]),len(grid))
        
        return count
        
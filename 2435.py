
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = [[[-1]*k for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return self.helper(grid,k,len(grid[0])-1,len(grid)-1,0, dp)



    def helper(self,grid, k, x, y, value, dp):
        MOD = 10**9 + 7
        
        if x < 0 or y < 0:
            return 0
        value += grid[y][x]
        value %= k
        if x == y and y == 0:
            if value == 0:
                return 1
            else:
                return 0

        if dp[y][x][value] != -1:
            return dp[y][x][value]
        down = self.helper(grid,k,x,y-1,value,dp)
        right = self.helper(grid,k,x-1,y,value,dp)
        dp[y][x][value] = (down+right)%MOD
        
        return dp[y][x][value]



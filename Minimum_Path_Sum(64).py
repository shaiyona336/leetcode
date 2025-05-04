def minPathSum(self, grid: List[List[int]]) -> int:
    if len(grid) == 0:
        return 0
    shortUntil = [[0 for i in row] for row in grid]
    shortUntil[0][0] = grid[0][0]
    for x in range(1,len(grid[0])):
        shortUntil[0][x] = shortUntil[0][x-1] + grid[0][x]
    for y in range(1,len(grid)):
        shortUntil[y][0] = shortUntil[y-1][0] + grid[y][0]
    for y in range(1,len(grid)):
        for x in range(1,len(grid[0])):
            currTileValue = grid[y][x]
            shortUntil[y][x] = min(shortUntil[y-1][x],shortUntil[y][x-1])+currTileValue

    return shortUntil[len(grid)-1][len(grid[0])-1]
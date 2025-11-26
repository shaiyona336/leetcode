class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        count = 0
        height = [0]*len(mat[0])

        for row in range(len(mat)):
            for column in range(len(mat[0])):
                if mat[row][column] == 1:
                    height[column] += 1
                else:
                    height[column] = 0

            for column in range(len(mat[0])):
                minHeight = float('inf')
                for indexMinHeight in range(column,-1,-1):
                    minHeight = min(minHeight,height[indexMinHeight])
                    count += minHeight

        return count

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        if size < 2:
            return
        for i in range(size//2):
            for j in range((size+1)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[size-1-j][i]
                matrix[size-1-j][i] = matrix[size-1-i][size-1-j]
                matrix[size-1-i][size-1-j] = matrix[j][size-1-i]
                matrix[j][size-1-i] = temp

                
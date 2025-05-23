ass Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        isZeroesFirstRow = any(matrix[0][j] for j in range(size)
        isZeroesFirstColumn = any(matrix[i][0] for i in range(size))

        for i in range(1,size):
            for j in range(1,size):
                if matrix[i][j] == 0:
                    matrix[0][j]=matrix[i][0]=0

        for i in range(1,size):
            for j in range(1,size):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if isZeroesFirstRow:
            for j in range(size):
                matrix[0][j]=0
        
        if izZeroesFirstColumn:
            for i in range(size):
                matrix[i][0]=0

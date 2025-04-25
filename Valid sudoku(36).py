class Solution:
    def isValidSudoku(self, board):
        
        validNine = set()

        #check rows
        for row in board:
            validNine.clear()
            for cell in row:
                if cell != ".":
                    if cell in validNine:
                        return False
                    validNine.add(cell)

        validNine.clear()
        #check columns
        for j in range(0,9):
            validNine.clear()
            for i in range(0,9):
                cell = board[i][j]
                if cell != ".":
                    if cell in validNine:
                        return False
                    validNine.add(cell)

        validNine.clear()
        #check boxes
        for y in range(0,3):
            for x in range(0,3):
                validNine.clear()
                for j in range(0,3):
                    for i in range(0,3):
                        cell = board[y*3+j][x*3+i]
                        if cell != ".":
                            if cell in validNine:
                                return False
                            validNine.add(cell)

        return True
    

# Example usage:
solution = Solution()
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(solution.isValidSudoku(sudoku_board))  # Output: True or False based on the validity of the Sudoku board
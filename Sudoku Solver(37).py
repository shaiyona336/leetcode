import copy
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        notSolvedYet = set()
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    board[row][column] = {1,2,3,4,5,6,7,8,9}
                    notSolvedYet.add((row,column))
        self.filterBoard(board,notSolvedYet)


    def removeValueFromIndex(self,board,row,column,value,modifyFlag):
        if len(board[row][column]) == 1:
            modifyFlag["flag"] = False
        elif len(board[row][column]) == 2:
            notSolvedYet.remove((row,i))
        else:
           board[row][column].remove(value)

    def filterByIndex(self,board,value,row,column,notSolvedYet,flag):
        #filter by row
        for i in range(9):
            if value in board[row][i]:
                self.removeValueFromIndex(board,row,i,value,flag)
        #filter by column
        for j in range(9):
            if value in board[j][column]:
                self.removeValueFromIndex(board,j,column,value,flag)
        #filter by box
        for i in range(row%3,row%3+3):
            for j in range(column%3,column%3+3):
                if value in board[i][j]:
                    self.removeValueFromIndex(board,i,j,value,flag)

        return notSolvedYet



    def filterBoard(self,board,notSolvedYet):
        modifyFlag = {"flag": True}
        for row in range(9):
            for column in range(9):
                if board[row][column] != '.':
                    value = board[row][column]
                    notSolvedYet = self.filterByIndex(board,value,row,column, notSolvedYet, modifyFlag)
                    if modifyFlag["flag"] == False:
                        return False
                else:
                    notSolvedYet.remove((row,column))
        if notSolvedYet == {}:
            return True
        isSolved
        while not isSolved:
            tryIndex = notSolvedYet.pop()
            valuesTryIndex = board[tryIndex[0]][tryIndex[1]]
            tryValue = valuesTryIndex.pop()
            board[tryIndex[0]][tryIndex[1]] = tryValue
            copyBoard = copy.deepcopy(board)
            isSolved = filterBoard(copyBoard,notSolvedYet)
            board = copyBoard
            if not isSolved:
                board[tryIndex[0]][tryIndex[1]] = valuesTryIndex

            if len(tryValue) == 1:
                notSolvedYet.remove(tryValue)
            self.filterBoard(board,notSolvedYet)
            
class Solution: 
    solutions = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        columns = [False]*n
        rightDiagnal = [False]*(2*n-1) #left to right if there is queen
        leftDiagnal = [False]*(2*n-1)
        self.solveNQueensHelper(n,0,leftDiagnal,rightDiagnal,columns,[])
        return self.solutions

        

    def solveNQueensHelper(self, n: int, row: int, leftDiagnal: List[bool], rightDiagnal: List[bool], columns: List[bool], solution: List[str]) -> List[List[str]]:
        if (row == n):
            self.solutions.append(solution[:])
            return

        
        for i in range(n):
            if rightDiagnal[row+i] or leftDiagnal[row-i+n-1] or columns[i]:
                continue
            rightDiagnal[row+i] = leftDiagnal[row-i+n-1] = columns[i] = True
            rowString = '.' * i + 'Q' + '.' * (n - i - 1)
            solution.append(rowString)
            self.solveNQueensHelper(n,row+1,leftDiagnal,rightDiagnal,columns,solution)
            rightDiagnal[row+i] = leftDiagnal[row-i+n-1] = columns[i] = False
            solution.pop()
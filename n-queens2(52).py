class Solution:
    count = 0
    def totalNQueens(self, n: int) -> int:
        columns = [False]*n
        rightDiagnal = [False]*(2*n-1)
        leftDiagnal = [False]*(2*n-1)
        self.helper(n,0, columns, leftDiagnal, rightDiagnal)
        return self.count
    


    def helper(self, n: int, x: int, columns, leftDiagnal, rightDiagnal) -> int:
        if x == n:
            self.count += 1
            return

        for i in range(n):
            if rightDiagnal[x+i] == True or leftDiagnal[x-i+n-1] == True or columns[i] == True:
                continue
            rightDiagnal[x+i] = leftDiagnal[x-i+n-1] = columns[i] = True
            self.helper(n,x+1,columns,leftDiagnal,rightDiagnal)
            rightDiagnal[x+i] = leftDiagnal[x-i+n-1] = columns[i] = False
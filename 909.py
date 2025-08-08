class Solution:
    def getXY(self,index,size):
        y=size-1-(index//size)
        isEvenLane = True if (index//size)%2==0 else False
        if isEvenLane:
            x = index % size
        else:
            x = size - 1 - index % size
        return x,y
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        size = len(board)
        nextMoves = deque([(0,0)]) #index:numberOfMoves
        visited = set()
        visited.add(0)
        maxSize=size**2-1

        while nextMoves:
            currMove,numMoves = nextMoves.popleft()
            for diceRoll in range(1,7):
                currMoveIndex = currMove+diceRoll
                if currMoveIndex>maxSize:
                    continue
                x,y = self.getXY(currMoveIndex,size)
                if board[y][x] != -1:
                    currMoveIndex=board[y][x]-1
                    x,y=self.getXY(currMoveIndex,size)
                if currMoveIndex in visited:
                    continue
                if currMoveIndex==maxSize:
                    return numMoves+1
                visited.add(currMoveIndex)
                nextMoves.append((currMoveIndex,numMoves+1))
        
        return -1

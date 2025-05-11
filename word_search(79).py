class Solution:
    def exist(self, board, word: str) -> bool:
        if len(board) == 0:
            return False if word != "" else True
        #alreadyStarted = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                alreadyBeen = set()
                if self.isWord(board,word,0,j,i,len(board[0]),len(board),alreadyBeen):
                    return True

        return False

    

    def isWord(self,board, word: str, currIndexWord: int, currIndexX: int, currIndexY: int, borderX: int, borderY: int, alreadyBeen: set):
        if len(word) == currIndexWord:
            return True
        if currIndexX < 0 or currIndexX >= borderX or currIndexY < 0 or currIndexY >= borderY:
            return False
        if board[currIndexY][currIndexX] != word[currIndexWord] or (currIndexX,currIndexY) in alreadyBeen:
            return False
        
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        for direction in directions:
            alreadyBeen.add((currIndexX,currIndexY))
            if self.isWord(board,word,currIndexWord+1,currIndexX+direction[0],currIndexY+direction[1],borderX,borderY,alreadyBeen):
                return True
            alreadyBeen.remove((currIndexX,currIndexY))

        return False
        


solution = Solution()

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word ="ABCB"
print(solution.exist(board,word))
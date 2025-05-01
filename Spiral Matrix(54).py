class Solution:
    def drawSquare(self, matrix):
        elements = []
        endFlag = False
        if not matrix or not matrix[0]:
            endFlag = True
            return (elements,endFlag)
        elif len(matrix) == 1:
            endFlag = True
            return (matrix[0],endFlag)
        elif len(matrix[0]) == 1:
            for i in range(len(matrix)):
                elements.append(matrix[i][0])
                endFlag = True
            return (elements,endFlag)
        
        for indexTopLine in range(len(matrix[0])):
            elements.append(matrix[0][indexTopLine])
        for indexRightLine in range(1,len(matrix)):
            elements.append(matrix[indexRightLine][len(matrix[0])-1])
        for indexBottomLine in range(1,len(matrix[0])):
            elements.append(matrix[len(matrix)-1][len(matrix[0])-1-indexBottomLine])
        for indexLeftLine in range(1,len(matrix)-1):
            elements.append(matrix[len(matrix)-1-indexLeftLine][0])
        return (elements,endFlag)

    def removeSquare(self, matrix):
        if matrix == None:
            return
        elif len(matrix) == 1:
            del matrix[0]
            return
        del matrix[0]
        del matrix[-1]
        for i in range(len(matrix)):
            del matrix[i][0]
            if len(matrix[0]) > 0:
                del matrix[i][-1]


    def spiralOrder(self, matrix):
        arrayToReturn = []
        newSquare = []
        endFlag = False
        for i in range(len(matrix),0,-2):
            newSquare,endFlag = self.drawSquare(matrix)
            arrayToReturn.extend(newSquare)
            if endFlag == True:
                return arrayToReturn
            self.removeSquare(matrix)
            

        return arrayToReturn
    

# Example usage:
solution = Solution()
matrix = [[3],[2]]
print(solution.spiralOrder(matrix))

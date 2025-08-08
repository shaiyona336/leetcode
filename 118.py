class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        toReturn = [[1]]
        for rowIndex in range(1,numRows):
            nextRow = []
            for indexInRow in range(rowIndex+1):
                if indexInRow==0 or indexInRow==rowIndex:
                    nextRow.append(1)
                else:
                    nextRow.append(toReturn[rowIndex-1][indexInRow-1]+toReturn[rowIndex-1][indexInRow])
            toReturn.append(nextRow)

        return toReturn

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
<<<<<<< HEAD
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
=======
        array = [[1]]
        index = 2
        size = 1
        while index <= numRows:
            currArray = [1]
            currIndexPrev = 0
            while currIndexPrev < size - 1:
                currArray.append(array[-1][currIndexPrev]+array[-1][currIndexPrev+1])
                currIndexPrev += 1
            currArray.append(1)
            array.append(currArray[:])
            size += 1
            index += 1

        return array
>>>>>>> ded088917894e5789a94480780c33e143e5ce9b7

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
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

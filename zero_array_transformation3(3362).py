class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        heap = []
        queries.sort()
        indexQuery = 0
        sizeQueries = len(queries)
        currOperations=0
        indexNotInOperation = [0]*(len(nums)+1)
        for i,num in enumerate(nums):
            currOperations+=indexNotInOperation[i]
            while indexQuery < sizeQueries and queries[indexQuery][0]==i:
                heappush(heap,-queries[indexQuery][1])
                indexQuery+=1
            while currOperations < num and heap and -heap[0]>=i:
                currOperations+=1
                indexNotInOperation[-heappop(heap)+1]-=1

            if currOperations<num:
                return -1

        return len(heap)

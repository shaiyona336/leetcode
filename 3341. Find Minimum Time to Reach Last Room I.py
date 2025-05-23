
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n=len(moveTime)
        if n > 0:
            m = len(moveTime[0])
        else:
            return 0

        visited = set()
        priorityQueue = [(0,(0,0))]
        distance = [[float('inf')]*m for i in range(n)]
        distance[0][0] = 0

        while priorityQueue:
            currDitanceFromStart,(currRow,currColumn) = heapq.heappop(priorityQueue)
            if (currRow,currColumn) in visited:
                continue
            visited.add((currRow,currColumn))
            #update neightbors
            neightbors = [(currRow-1,currColumn),(currRow+1,currColumn),(currRow,currColumn-1),(currRow,currColumn+1)]
            for neigborRow,neigborColumn in neightbors:
                if neigborRow >= 0 and neigborColumn >= 0 and neigborRow < n and neigborColumn < m:
                    newPotentialyDistance = distance[currRow][currColumn] + 1
                    if newPotentialyDistance < distance[neigborRow][neigborColumn]:
                        newPotentialyDistance = max(moveTime[neigborRow][neigborColumn]+1,newPotentialyDistance)
                        distance[neigborRow][neigborColumn] = newPotentialyDistance
                        heapq.heappush(priorityQueue,(newPotentialyDistance,(neigborRow,neigborColumn)))

        return distance[n-1][m-1] if distance[n-1][m-1] != float('inf') else -1

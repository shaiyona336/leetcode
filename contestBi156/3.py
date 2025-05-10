import copy
class Solution:
        def maxWeight(self, n: int, edges, k: int, t: int) -> int:
            maxPath = -1
            if k == 0:
                 return 0
            for edge in edges:
                newEdges = copy.deepcopy(edges)
                newEdges.remove(edge)
                currSum = self.helper(n,newEdges,k-1,edge[2],t,edge[1])
                if currSum == -1:
                    continue
                maxPath = max(maxPath,currSum)


            return maxPath



        def helper(self, n: int, edges, k: int, t: int, limit: int, currU: int) -> int:
            maxPath = -1
            if t >= limit:
                 return -1
            if k == 0:
                 return t
            for edge in edges:
                if edge[0] != currU:
                     continue
                newEdges = copy.deepcopy(edges)
                newEdges.remove(edge)
                currSum = self.helper(n,newEdges,k-1,t+edge[2],limit,edge[1])
                if currSum == -1:
                    continue
                maxPath = max(maxPath,currSum)

            return maxPath
            

n = 3
edges = [[0,1,1],[1,2,2]]
k = 2
t = 4
sol = Solution()
print(sol.maxWeight(n, edges, k, t))  # Output: 3
n = 3
edges = [[0,1,2],[0,2,3]]
k = 1
t = 3
sol = Solution()
print(sol.maxWeight(n, edges, k, t))  # Output: 3
n = 3
edges = [[0,1,6],[1,2,8]]
k = 1
t = 6
sol = Solution()
print(sol.maxWeight(n, edges, k, t))  # Output: 3
n = 4
edges = [[0,2,3],[1,3,10],[0,3,5],[2,3,10],[0,1,1]]
k = 2
t = 38
sol = Solution()
print(sol.maxWeight(n, edges, k, t))  # Output: 13












class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        size = len(gas)
        startingPos = 0
        currGas = 0
        totalGas = 0

        for i in range(size):
            currCost = gas[i] - cost[i]
            currGas += currCost
            totalGas += currCost
            if currGas < 0:
                startingPos = i + 1
                currGas = 0
        if totalGas >= 0:
            return startingPos
        return -1
        
# Example usage:
solution = Solution()
gas = [2,3,4]
cost = [3,4,3]
print(solution.canCompleteCircuit(gas, cost))  # Output: 3
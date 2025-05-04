class Solution:
    def minimumCardPickup(self, cards) -> int:
        alreadySeen = {}
        howMany = float('inf')
        minHowMany = float('inf')

        for index in range(0,len(cards)):
            if cards[index] in alreadySeen:
                howMany = index - alreadySeen[cards[index]] + 1
                minHowMany = min(minHowMany,howMany)
            alreadySeen[cards[index]] = index

        return minHowMany if howMany != float('inf') else -1
    

# Example usage:
solution = Solution()
cards = [77,10,11,51,69,83,33,94,0,42,86,41,65,40,72,8,53,31,43,22,9,94,45,80,40,0,84,34,76,28,7,79,80,93,20,82,36,74,82,89,74,77,27,54,44,93,98,44,39,74,36,9,22,57,70,98,19,68,33,68,49,86,20,50,43]
result = solution.minimumCardPickup(cards)
print(result)  # Output: 4 (the minimum number of consecutive cards to pick up is 4)

from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        count = 0
        alreadySeenDominoes = defaultdict(int)
        
        for domino in dominoes:
            sortedDomino = tuple(sorted(domino))
            count += alreadySeenDominoes[sortedDomino]
            alreadySeenDominoes[sortedDomino] += 1

        return count
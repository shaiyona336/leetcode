class Solution:
    def maxDifference(self, s: str) -> int:
        freq = defaultdict(int)
        maxDiff = float('-inf')

        for char in s:
            freq[char]+=1

        minOdd = float('inf')
        maxOdd = 0

        for char in s:
            if freq[char] % 2 == 1:
                minOdd = min(minOdd,freq[char])
                maxOdd = max(maxOdd,freq[char])

        for char in s:
            if freq[char] % 2 == 0:
                maxDiff = max(maxDiff,maxOdd-freq[char])
                maxDiff = max(maxDiff,minOdd-freq[char])

        return maxDiff

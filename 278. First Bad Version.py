import math
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            median = left + math.floor((right-left)/2)
            if not isBadVersion(median):
                left = median + 1
            else:
                right = median - 1

        return left if isBadVersion(left) else left+1

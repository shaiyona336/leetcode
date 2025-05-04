class Solution:
    def wordPattern(self, pattern, s):
        alreadySeen = {}
        s = s.split()
        pattern = list(pattern)
        if len(pattern) != len(s):
            return False
        for index in range(len(pattern)):
            currLatter = pattern[index]
            if currLatter in alreadySeen:
                if alreadySeen[currLatter] != s[index]:
                    return False
            else:
                if s[index] in alreadySeen.values():
                    return False
                alreadySeen[currLatter] = s[index]

        return True
    
# Example usage:
solution = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(solution.wordPattern(pattern, s))
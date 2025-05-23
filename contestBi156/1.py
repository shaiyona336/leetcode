class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        others = {}
        maxVowels = 0
        maxConsonants = 0

        for char in s:
            if char in vowels:
                if char in vowels:
                    vowels[char] += 1
            else:
                if char in others:
                    others[char] += 1
                else:
                    others[char] = 1

        for vowel in vowels:
            currValue = vowels[vowel]
            maxVowels = max(maxVowels,currValue)

        for other in others:
            currValue = others[other]
            maxConsonants = max(maxConsonants,currValue)
        return maxConsonants+maxVowels



solution = Solution()
print(solution.maxFreqSum("successes"))

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        maxPrefix = 0
        amountStrings = len(strs)
        indexWord = 0
        minLen = min([len(string) for string in strs])
        currLetter = ''
        continueFlag = True

        if (amountStrings == 0):
            return 0
        while (maxPrefix < minLen and continueFlag):
            if (indexWord == 0):
                currLetter = strs[0][maxPrefix]
                indexWord += 1
            else:
                if indexWord == amountStrings:
                    indexWord = 0
                    maxPrefix += 1
                elif indexWord == amountStrings - 1:
                    if (strs[indexWord][maxPrefix] != currLetter):
                        continueFlag = False
                    else:
                        indexWord = 0
                        maxPrefix += 1
                else:
                    if (strs[indexWord][maxPrefix] != currLetter):
                        continueFlag = False
                    else:
                        indexWord += 1

        return strs[0][0:maxPrefix]
    

solution = Solution()
print(solution.longestCommonPrefix(["a"])) # Expected output: "fl"
        
        
        
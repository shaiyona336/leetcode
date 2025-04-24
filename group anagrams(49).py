class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        listToReturn = []
        sortLetters = {}
        maxSameWord = 0
        indexCurrWordInList = 0

        for word in strs:
            sortLetters[word] = ''.join(sorted(word))
        
        for word in strs:
            indexCurrWordInList = 0
            while (True):
                if (indexCurrWordInList == maxSameWord):
                    listToReturn.append([word])
                    maxSameWord += 1
                    break
                elif (sortLetters[listToReturn[indexCurrWordInList][0]] == sortLetters[word]):
                    listToReturn[indexCurrWordInList].append(word)
                    break
                else:
                    indexCurrWordInList += 1
        
        return listToReturn
    

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # Expected output: [["bat"],["nat","tan"],["ate","eat","tea"]]
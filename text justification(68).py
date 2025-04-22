class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        stringToReturn = []
        currLine = ""
        wordsInCurrLine = []
        numSpacesInCurrLine = 0
        numLettersCurrLine = 0
        leftMostExtraSpacesCurrLine = 0
        minimumSpacesCurrLine = 0
        wordIndex = 0

        while wordIndex < len(words):
            if (numLettersCurrLine == 0):
                wordsInCurrLine.append(words[wordIndex])
                numLettersCurrLine += len(words[wordIndex])
                wordIndex += 1
            elif (numLettersCurrLine + len(words[wordIndex]) + 1 <= maxWidth):
                wordsInCurrLine.append(words[wordIndex])
                numLettersCurrLine += len(words[wordIndex]) + 1
                wordIndex += 1
            else:
                #the spaces that we'll need in the line is the spaces left (maxWidth-numLettersCurrLine) minus the spaces that i already added minimum one between any two words
                numSpacesInCurrLine = maxWidth - (numLettersCurrLine - (len(wordsInCurrLine) - 1))
                if (len(wordsInCurrLine) > 1):
                    minimumSpacesCurrLine = int(numSpacesInCurrLine / (len(wordsInCurrLine) - 1))
                else:
                    minimumSpacesCurrLine = maxWidth - numLettersCurrLine
                if (len(wordsInCurrLine) > 1):
                    leftMostExtraSpacesCurrLine = int(numSpacesInCurrLine % (len(wordsInCurrLine) - 1))
                else:
                    leftMostExtraSpacesCurrLine = int(numSpacesInCurrLine % len(wordsInCurrLine))
                for wordInCurrLine in wordsInCurrLine:
                    if (currLine == ""):
                        currLine += wordInCurrLine
                        if (len(wordsInCurrLine) == 1):
                            currLine += " "*(maxWidth-len(currLine))
                    else:
                        currLine += minimumSpacesCurrLine * " "
                        if (leftMostExtraSpacesCurrLine > 0):
                            currLine += " "
                        leftMostExtraSpacesCurrLine -= 1 if leftMostExtraSpacesCurrLine > 0 else 0
                        currLine += wordInCurrLine
                #stringToReturn += currLine + "\n"
                stringToReturn.append(currLine)
                numSpacesInCurrLine = 0
                numLettersCurrLine = 0
                currLine = ""
                wordsInCurrLine = []
        #last line
        if (wordsInCurrLine != []):
            for wordInCurrLine in wordsInCurrLine:
                if (currLine == ""):
                    currLine += wordInCurrLine
                else:
                    currLine += " " + wordInCurrLine
            currLine += " "*(maxWidth-len(currLine))
            stringToReturn.append(currLine)

        return stringToReturn
    


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

solution = Solution()
result = solution.fullJustify(words, maxWidth)
print(result)
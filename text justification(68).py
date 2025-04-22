def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    stringToReturn = ""
    currLine = ""
    wordsInCurrLine = []
    numSpacesInCurrLine = 0
    numLettersCurrLine = 0
    leftMostExtraSpacesCurrLine = 0
    minimumSpacesCurrLine = 0

    for word in words:
        if (numLettersCurrLine == 0):
            wordsInCurrLine.append(word)
            numLettersCurrLine += len(word)
        elif (numLettersCurrLine + len(word) + 1 <= maxWidth):
                wordsInCurrLine.append(word)
                numLettersCurrLine += len(word) + 1
        else:
            #the spaces that we'll need in the line is the spaces left (maxWidth-numLettersCurrLine) minus the spaces that i already added minimum one between any two words
            numSpacesInCurrLine = maxWidth - (numLettersCurrLine - (len(wordsInCurrLine) - 1))
            minimumSpacesCurrLine = int(numSpacesInCurrLine / (len(wordsInCurrLine) - 1))
            leftMostExtraSpacesCurrLine = int(numSpacesInCurrLine % (len(wordsInCurrLine) - 1))
            for wordInCurrLine in wordsInCurrLine:
                if (currLine == ""):
                    currLine += wordInCurrLine
                else:
                    currLine += minimumSpacesCurrLine * " "
                    currLine += leftMostExtraSpacesCurrLine * " "
                    leftMostExtraSpacesCurrLine -= 1 if leftMostExtraSpacesCurrLine > 0 else 0
                    currLine += wordInCurrLine
            stringToReturn += currLine + "\n"
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
        stringToReturn += currLine

        return stringToReturn
    


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(fullJustify(words, maxWidth))

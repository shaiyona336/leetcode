class Solution:
    def resize(self,a,b,diff): #resize b to size of a (b<a)
        b = "0"*diff + b
        return b

    def addBinary(self,a,b):
        leftOver = False
        newNum = ""
        currIndex = 0 #index from right
        sizeA = len(a)
        sizeB = len(b)
        
        if sizeA > sizeB:
            b = self.resize(a,b,sizeA-sizeB)
        elif sizeB > sizeA:
            a = self.resize(b,a,sizeB-sizeA)
        maxSize = max(sizeA,sizeB)

        while currIndex < maxSize:
            #need to define next char, and leftOver
            #define next char
            newChar = bool(int(a[maxSize-1-currIndex])) ^ bool(int(b[maxSize-1-currIndex])) ^ leftOver
            newChar = '1' if newChar else '0'
            newNum = newChar + newNum
            #define leftOver
            leftOverInt = 1 if leftOver else 0
            intIndexA = int(a[maxSize-1-currIndex])
            intIndexB = int(b[maxSize-1-currIndex])
            leftOver = True if (leftOverInt + intIndexA + intIndexB) >= 2 else False
            currIndex += 1

        if leftOver:
            newNum = '1' + newNum
            
        return newNum
            
        

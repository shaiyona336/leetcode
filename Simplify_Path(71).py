class Solution:
    def doubleDot(self,path):  # if the next folder is .. need to remove last folder
        words = path.split("/")
        newPath = "/"

        for wordIndex in range(1, len(words) - 2):
            currWord = words[wordIndex]
            newPath += currWord + "/"

        return newPath if newPath != "" else "/"


    def simplifyPath(self, path: str) -> str:
        currIndex = 1
        size = len(path)
        newPath = "/"
        if len(newPath) < 1 or path[0] != '/':
            return newPath
        isSlashMode = True
        nextFolder = ""
        while currIndex < size:
            while isSlashMode and currIndex < size:
                if path[currIndex] == '/':
                    currIndex += 1
                else:
                    isSlashMode = False
            while not isSlashMode and currIndex < size:
                if path[currIndex] != '/':
                    nextFolder += path[currIndex]
                    currIndex += 1
                else:
                    isSlashMode = True
            if nextFolder == ".":
                pass
            elif nextFolder == "..":
                newPath = self.doubleDot(newPath)
            else:
                newPath += nextFolder + "/"

            currIndex += 1
            nextFolder = ""
        
        while len(newPath) > 1 and newPath[-1] == "/":
            newPath = newPath[:-1]

        return newPath


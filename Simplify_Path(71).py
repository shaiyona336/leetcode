def doubleDot(path): #if the next folder is .. need to remove last folder
    words = newPath.split("")
    newPath = ""

    for wordIndex in range(1,len(path)-1)
        newPath += "/" + path[word]

    return newPath if newPath != "" else "/"


def simplifyPath(path):
  currIndex = 1
  size = len(newPath)
  newPath = '/'
  if len(newPath) < 1 or path[0] != '/':
    return newPath
  isSlashMode = True
  nextFolder = ""
  while currIndex < size:
    while isSlashMode and currIndex < size:
      if path[currIndex] = '/':
        currIndex += 1
      else:
        isSlashMode = False
    while not isSlashMode and currIndex < size:
        if path[currIndex] != '/':
            nextFolder += newPath
            currIndex += 1
        else:
            isSlashMode = True
    if nextFolder == ".":
        pass
    elif nextFolder == "..":
        doubleDot(newPath)
    else:
        newPath += nextFolder

    currIndex += 1

def lengthOfLongestSubstring(s):
  alreadySeen = set()
  maxNoDup = 0
  size = len(s)
  leftIndex = 0
  rightIndex = 1

  if size == 0:
      return 0
  elif size == 1:
      return 1
  currString = s[0]
  alreadySeen.add(s[0])
  while rightIndex < size:
     if s[rightIndex] not in alreadySeen:
        alreadySeen.add(s[rightIndex])
        currString += s[rightIndex]
        rightIndex += 1
        maxNoDup = max(maxNoDup, len(currString))
     else:
        alreadySeen.remove(s[leftIndex])
        leftIndex += 1
        currString = s[leftIndex:rightIndex]
  return maxNoDup
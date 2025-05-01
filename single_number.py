def singleNumber(nums):
    nums = sorted(nums)
    lastNumber = nums[0]
    currIndex = 1
    currPairCount = 1
    size = len(nums)

    while True:
        if currIndex >= size - 1:
            return nums[size-1]
        elif nums[currIndex] != lastNumber and currPairCount == 1:
            return lastNumber
        elif currPairCount == 1:
            currPairCount = 0
        else: #currPair = 0
            currPairCount = 1
            lastNumber = nums[currIndex]
        currIndex += 1




ass Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.toReturn = []
        self.helper(toReturn)
        return toReturn

    def helper(self, currSub, nums):
        if nums == []:
            if currSub!=[]:
                self.toReturn.append(currSub[:])

        for num in nums:
            currSub.append(num)
            nums.remove(num)
            self.helper(currSub,nums)
            nums.add(num)
            currSub.remove(num)


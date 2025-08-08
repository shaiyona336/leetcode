class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        toReturn = []
        inFirstArray = set()

        for num in nums1:
            inFirstArray.add(num)

        for num in nums2:
            if num in inFirstArray:
                toReturn.insert(num)
                inFirstArray.append(num)

        return toReturn

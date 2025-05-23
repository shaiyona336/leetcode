class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        size = len(nums)
        toReturn = []
        alreadySeen = set()

        for i in range(size):
            if i > 0 and i <= size - 1 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = size - 1

            while left < right:
                currValue = nums[i] + nums[left] + nums[right]
                if currValue == 0:
                    triplet = (nums[i], nums[left], nums[right])
                    if triplet not in alreadySeen:
                        toReturn.append(triplet)
                        alreadySeen.add(triplet)
                    right -= 1
                elif currValue > 0:
                    right -= 1
                else:
                    left += 1

        return toReturn
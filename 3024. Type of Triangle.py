class Solution:
    def can_form_triangle(self, nums):
        if nums[0]+nums[1]>nums[2]:
            return True
        return False


    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if not self.can_form_triangle(nums):
            return "none"
        if nums[0]==nums[1]==nums[2]:
            return "equilateral"
        elif nums[0]==nums[1] or nums[0]==nums[2] or nums[1]==nums[2]:
            return "isosceles"
        return "scalene"

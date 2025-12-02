class Solution:
    def is_possible(self, n, batteries, time):
        energy_given = 0

        for battery in batteries:
            energy_given += min(battery,time)
        if energy_given >= n*time:
            return True

        return False


    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left = 0
        right = sum(batteries) // n

        while left < right:
            mid = (left+right+1)//2
            if self.is_possible(n,batteries,mid):
                left = mid
            else:
                right = mid-1

        return left

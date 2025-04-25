class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        alreadySeen = set()
        
        for i in range(0,len(nums)):
            if nums[i] in alreadySeen:
                return True
            alreadySeen.add(nums[i])
            if(len(alreadySeen) > k):
                alreadySeen.remove(nums[i-k])
            
        return False
    

solution = Solution()
print(solution.containsNearbyDuplicate([99,99], 2)) # Expected output: True
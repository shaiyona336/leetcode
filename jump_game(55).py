class Solution:
    def canJump(self, nums) -> bool:
        size = len(nums)
        canGetIndex = [False]*(size)
        if size > 0:
            canGetIndex[0]=True
        for index in range(len(nums)):
            if canGetIndex[index]==True:
                for j in range(1,nums[index]+1):
                    if index+j >= size:
                        break
                    canGetIndex[index+j]=True
        
        return canGetIndex[size-1]


        


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums=[2,3,1,1,4]
    print(solution.canJump(nums))  # Output: True
    nums = [3,2,1,0,4]
    print(solution.canJump(nums))  # Output: False
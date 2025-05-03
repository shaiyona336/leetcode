class Solution:
    def maxArea(self,height):
        maxSum = 0

        for i in range(len(height)-1):
          for j in range(i+1,len(height)):
            sum = (min(height[i],height[j])) * (j-i)
            if sum > maxSum:
              maxSum = sum

        return maxSum


# Example usage:
solution = Solution()
height = [8,7,2,1]
print(solution.maxArea(height))

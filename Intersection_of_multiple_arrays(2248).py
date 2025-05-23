class Solution:
    def intersection(self, nums):
        inAll = set()

        for array in nums:
            for num in array:
                inAll.add(num)

        for num in list(inAll):
            for array in nums:
                if num not in array and num in inAll:
                    inAll.remove(num)
        
        return list(inAll)
        

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
    print(solution.intersection(nums))  # Output: [1, 2]
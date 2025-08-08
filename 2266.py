class Solution:
    def remap(self, num, fromChar, toChar):
        num = str(num)
        for charIndex in range(len(num)):
            if num[charIndex]==fromChar:
                num=num[:charIndex]+toChar+num[charIndex+1:]
        
        return int(num)

    def minMaxDifference(self, num: int) -> int:
        minNum = float('inf')
        maxNum = float('-inf')
        toReturn = 0

        for digitFrom in range(10):
            for digitTo in range(10):
                if digitFrom==digitTo:
                    continue
                currNum = self.remap(num,str(digitFrom),str(digitTo))
                minNum = min(minNum,currNum)
                maxNum = max(maxNum,currNum)
                
        
        return abs(maxNum-minNum)
    

if __name__ == "__main__":
    num = 11891
    solution = Solution()
    print(solution.minMaxDifference(num))
class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        index = 0
        dp = [-1]*size
        return self.helper(s,index,size,dp)
        

    def helper(self, s, index, size, dp):
        if (index >= size):
            return 1
        if (s[index] == '0'):
            return 0
        if (dp[index] != - 1):
            return dp[index]
        #take first digit
        ways = self.helper(s,index+1,size,dp)
        #take two digits
        if index + 1 < size:
            if s[index] == '1' or (s[index] == '2' and s[index+1] <= '6'):
                ways += self.helper(s,index+2,size,dp)

        dp[index] = ways
        return dp[index]
        





#f(s) = number of ways to decode s
#if s[0] in {0,3,4,5,6,7,8,9} => f(s) = 0
#else
#if (s[0] = 2 and s[1] in {7,8,9]) => then first character is the digit=>
#f(s)=f(s[1:])
#else
#f(s)=f(s[1:])+f(s[2:])
        

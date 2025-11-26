class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n>=k+maxPts:
            return 1
        dp = [0]*(k+maxPts+1)
        for i in range(n+1,k+maxPts+1):
            dp[i] = 0
        for i in range(k,n+1):
            dp[i] = 1
        windowSum = n-k+1 #x>n->dp[x]=0, k<=x<=n->dp[x]=1
        for i in range(k-1,-1,-1):
            dp[i] = windowSum/maxPts
            windowSum += dp[i]-dp[i+maxPts]

        return dp[0]


class Solution:
    def tribonacci(self, n: int) -> int:
        dp =[0]*(n+1)
        dp[1] =1 
        def depth(n):
            if n<=0:
                return 0
            if dp[n]!=0:
                return dp[n]
            dp[n] = depth(n-1) + depth(n-2) + depth(n-3)
            return dp[n]
        return depth(n)
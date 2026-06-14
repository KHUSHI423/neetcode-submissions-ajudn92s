class Solution:
    def climbStairs(self, n: int) -> int:
        #top - dowm 
        dp = [-1 for _ in range(n+1)]
        def solve(i,dp):
            if i<=2:
                return i
            if dp[i] != -1:
                return dp[i]
            dp[i] = solve(i-1,dp) + solve(i-2,dp)
            return dp[i]
        
        return solve(n,dp)
        '''
        #recurrsive
        if n <=2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''
class Solution:
    def climbStairs(self, n: int) -> int:
        # SPACE OPTIMIZATION
        p1 = 1
        p2 = 1
        curr = 0
        while (n-1):
            curr = p1 + p2
            p2 = p1
            p1 = curr
            n-=1
        return p1

        '''
        #bottom top
        dp =[ 0 for _ in range(n+1)]
        dp[0] =1
        dp[1] =1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        
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
        
        #recurrsive
        if n <=2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''
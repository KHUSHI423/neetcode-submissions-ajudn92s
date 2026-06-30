class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=  [[-1]*n for _ in range(m)]
        def dfs(m,n,dp,i=0,j=0):
            if i>=m or j>=n:
                return 0
            if i == m-1 and j ==n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j] = dfs(m,n,dp,i+1,j) + dfs(m,n,dp,i,j+1)
            return dp[i][j]
        
        return dfs(m,n,dp)
        
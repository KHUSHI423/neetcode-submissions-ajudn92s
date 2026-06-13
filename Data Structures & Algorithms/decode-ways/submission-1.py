class Solution:
    def numDecodings(self, s: str) -> int:
        
        #top - bottom
        def dfs(i,s,dp):
            if i >= len(s):
                return 1
            if s[i] =='0':
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = dfs(i+1,s,dp)
            if i < len(s) -1:
                if s[i] == '1' or (s[i] =='2' and s[i+1] <'7'):
                    dp[i]+=dfs(i+2,s,dp)
            return dp[i]

        dp = [-1 for _ in range(len(s)+1)]
        return dfs(0,s,dp)
        
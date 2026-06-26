class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n  = len(grid)
        m = len(grid[0])
        vis =[[0]*m for _ in range(n)]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j,vis):
            vis[i][j] = 1
            count = 1
            for r,c in dirs:
                dr = i + r
                dc = j + c
                if (0<=dr<n and 0<=dc<m and grid[dr][dc] == 1 and vis[dr][dc] == 0):
                    count += dfs(dr,dc,vis)
            return count

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    ans = max(ans,dfs(i,j,vis))
        return ans 
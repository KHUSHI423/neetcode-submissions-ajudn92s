class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]
        dirs  = [(-1,0),(1,0),(0,-1),(0,1)]
        def solve(i , j , vis):
            vis[i][j] = 1
            for r,c in dirs:
                dr = i+r
                dc = j +c
                if(0<=dr<n and
                    0<=dc <m and
                    grid[dr][dc] == "1" and
                    vis[dr][dc] == 0 ):
                    solve(dr,dc,vis)
            return 1

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and vis[i][j] == 0:
                    ans += solve(i,j,vis)
        return ans

        
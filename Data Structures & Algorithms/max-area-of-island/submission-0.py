class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        def bfs(i,j,grid,vis):
            vis[i][j] = 1
            c = 1
            queue = deque([(i,j)])
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while queue:
                curr_row, curr_col = queue.popleft()
                for dr,dc in dirs:
                
                    row = curr_row+dr
                    col = curr_col+dc
                    if row >=0 and row< len(grid) and col >=0 and col<len(grid[0]) and grid[row][col] == 1 and vis[row][col]!=1:
                        vis[row][col] =1
                        c+=1
                        queue.append((row,col))
            return c
        vis=[[0]*(m) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j]!=1:
                    cnt= max(cnt,bfs(i,j,grid,vis))
        return cnt
        
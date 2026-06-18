class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        visited =[[0]*m for _ in range(n)]
        def bfs(r,c,vis):
            vis[r][c] = 1
            queue =deque([(r,c)])
            while queue:
                row,col = queue.popleft()
                dirs= [(1,0),(-1,0),(0,1),(0,-1)]
                for i,j in dirs:
                    dr = row + i
                    dc = col + j
                    if (dr>=0 and
                        dc>=0 and 
                        dr<len(grid) and
                        dc<len(grid[0]) and
                        grid[dr][dc] == '1' and 
                        vis[dr][dc]!=1):
                        vis[dr][dc]=1
                        queue.append((dr,dc))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j]!= 1:
                    res+=1
                    bfs(i,j,visited)
        return res

        '''
        n = len(grid)
        m = len(grid[0])
        count = 0 
        def dfs(r,c):
            if (r <0 or
                c<0 or
                r>=len(grid) or
                c>=len(grid[0]) or
                grid[r][c] == '0'
                ):
                return 
            grid[r][c] = '0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        return count
        '''

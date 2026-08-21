class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            for _ in range(len(q)):
                row,col = q.popleft()
                
                for i,j in dirs:
                    dr = row + i
                    dc = col + j
                    if (0<=dr<n and 
                    0<=dc<m and 
                    grid[dr][dc]==2147483647 ):
                        grid[dr][dc] = 1+ grid[row][col]
                        q.append((dr,dc))
                        
        
        


        
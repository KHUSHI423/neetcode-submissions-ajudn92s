class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        if fresh == 0:
            return 0
        min = 0
        while q and fresh>0:
            
           
            s= len(q)
            for _ in range(s):
                row,col = q.popleft()
                for i,j in dirs:
                    dr = row + i
                    dc = col + j
                    if (0<=dr<n and
                        0<=dc<m and
                        grid[dr][dc]==1 ):
                        fresh-=1
                        grid[dr][dc] = 2
                        q.append((dr,dc))
            min+=1
        return min if fresh == 0 else -1
            



        
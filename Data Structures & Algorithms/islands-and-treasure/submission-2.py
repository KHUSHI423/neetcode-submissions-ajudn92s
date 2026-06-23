class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n = len(grid)
        m = len(grid[0])

        q = deque()

        # Put all gates into queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:

            row, col = q.popleft()

            for dr, dc in dirs:

                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < n and
                    0 <= nc < m and
                    grid[nr][nc] == 2147483647
                ):

                    # distance = parent distance + 1
                    grid[nr][nc] = grid[row][col] + 1

                    q.append((nr, nc))
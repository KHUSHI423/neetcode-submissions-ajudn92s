class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        n = len(heights)
        m = len(heights[0])

        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r, c, vis):
            vis[r][c] = True

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and
                    0 <= nc < m and
                    not vis[nr][nc] and
                    heights[nr][nc] >= heights[r][c]):   # reverse condition

                    dfs(nr, nc, vis)

        # Pacific (top row)
        for j in range(m):
            dfs(0, j, pacific)

        # Pacific (left column)
        for i in range(n):
            dfs(i, 0, pacific)

        # Atlantic (bottom row)
        for j in range(m):
            dfs(n - 1, j, atlantic)

        # Atlantic (right column)
        for i in range(n):
            dfs(i, m - 1, atlantic)

        ans = []

        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans
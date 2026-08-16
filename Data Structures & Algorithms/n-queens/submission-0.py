class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        matrix = [["."] * n for _ in range(n)]
        ans = []

        def fill_dp(dp, i, j):

            # Same row
            for k in range(n):
                dp[i][k] = 1

            # Same column
            for k in range(n):
                dp[k][j] = 1

            # Upper-left ↖
            k = i - 1
            l = j - 1
            while k >= 0 and l >= 0:
                dp[k][l] = 1
                k -= 1
                l -= 1

            # Upper-right ↗
            k = i - 1
            l = j + 1
            while k >= 0 and l < n:
                dp[k][l] = 1
                k -= 1
                l += 1

            # Lower-left ↙
            k = i + 1
            l = j - 1
            while k < n and l >= 0:
                dp[k][l] = 1
                k += 1
                l -= 1

            # Lower-right ↘
            k = i + 1
            l = j + 1
            while k < n and l < n:
                dp[k][l] = 1
                k += 1
                l += 1

        def solve(row, dp):

            # All n queens have been placed
            if row == n:
                board = []

                for i in range(n):
                    board.append("".join(matrix[i]))

                ans.append(board)
                return

            # Try every column in this row
            for col in range(n):

                # Position is already attacked
                if dp[row][col] == 1:
                    continue

                # Place queen
                matrix[row][col] = "Q"

                # Create a new dp for this choice
                new_dp = [r[:] for r in dp]

                # Mark cells attacked by this queen
                fill_dp(new_dp, row, col)

                # Go to next row
                solve(row + 1, new_dp)

                # BACKTRACK
                matrix[row][col] = "."

        dp = [[0] * n for _ in range(n)]

        solve(0, dp)

        return ans
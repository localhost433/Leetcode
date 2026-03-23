class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        dp = [[0, 0] * (n+1) for _ in range(m+1)]
        dp[0][0] = (grid[0][0], grid[0][0])

        for i in range(1, m):
            val = grid[i][0] * dp[i-1][0][0]
            dp[i][0] = (val, val)

        for j in range(1, n):
            val = grid[0][j] * dp[0][j-1][0]
            dp[0][j] = (val, val)

        for i in range(1, m):
            for j in range(1, n):
                tup = [
                    grid[i][j] * dp[i-1][j][0], grid[i][j] * dp[i-1][j][1],
                    grid[i][j] * dp[i][j-1][0], grid[i][j] * dp[i][j-1][1]
                ]
                dp[i][j] = (max(tup), min(tup))
        ret = dp[m-1][n-1][0]
        return ret % MOD if ret >= 0 else -1
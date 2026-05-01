class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[ -1 for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]
        def val_cost(num):
            score = num
            cost = 1 if num == 2 else num
            return score, cost
        s0, c0 = val_cost(grid[0][0])
        if c0 <= k:
            dp[0][0][c0] = s0
        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == -1:
                        continue
                    for di, dj in [(0, 1), (1, 0)]:
                        ni, nj = i + di, j + dj
                        if ni < m and nj < n:
                            s_next, c_next = val_cost(grid[ni][nj])
                            if c + c_next <= k:
                                dp[ni][nj][c + c_next] = max(dp[ni][nj][c + c_next], dp[i][j][c] + s_next)
        ans = max(dp[m-1][n-1])
        return ans if ans != -1 else -1
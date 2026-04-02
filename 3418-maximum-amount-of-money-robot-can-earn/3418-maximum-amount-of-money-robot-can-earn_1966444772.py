class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[0] * 3 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = max(coins[0][0], 0)
        dp[0][0][2] = max(coins[0][0], 0)
        for i in range(1, m):
            cur = coins[i][0]
            val = max(cur, 0)
            dp[i][0][0] = dp[i-1][0][0] + cur
            dp[i][0][1] = max(dp[i-1][0][1] + cur, dp[i-1][0][0] + val)
            dp[i][0][2] = max(dp[i-1][0][2] + cur, dp[i-1][0][1] + val)
        for j in range(1, n):
            cur = coins[0][j]
            val = max(cur, 0)
            dp[0][j][0] = dp[0][j-1][0] + cur
            dp[0][j][1] = max(dp[0][j-1][1] + cur, dp[0][j-1][0] + val)
            dp[0][j][2] = max(dp[0][j-1][2] + cur, dp[0][j-1][1] + val)
        for i in range(1, m):
            for j in range(1, n):
                cur = coins[i][j]
                val = max(cur, 0)
                dp[i][j][0] = max(dp[i-1][j][0] + cur, dp[i][j-1][0] + cur)
                dp[i][j][1] = max(dp[i-1][j][0] + val, dp[i][j-1][0] + val,
                                    dp[i-1][j][1] + cur, dp[i][j-1][1] + cur)
                dp[i][j][2] = max(dp[i-1][j][2] + cur, dp[i][j-1][2] + cur,
                                    dp[i-1][j][1] + val, dp[i][j-1][1] + val)
        return max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])
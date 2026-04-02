class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[-inf] * 3 for _ in range(n+1)]
        dp[1] = [0] * 3
        for i in range(m):
            for j in range(n):
                cur = coins[i][j]
                u0, u1, u2 = dp[j+1]
                l0, l1, l2 = dp[j]
                dp[j+1][0] = max(u0, l0) + cur
                dp[j+1][1] = max(u1 + cur, l1 + cur, u0, l0)
                dp[j+1][2] = max(u2 + cur, l2 + cur, u1, l1)
        return dp[n][2]
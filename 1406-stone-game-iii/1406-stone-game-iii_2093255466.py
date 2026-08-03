class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        dp[n] = 0
        dp[n-1] = stoneValue[n-1]

        if n >= 2:
            dp[n-2] = max(stoneValue[n-2] - dp[n-1], stoneValue[n-2] + stoneValue[n-1])

        for i in range(n-3, -1, -1):
            dp[i] = max(
                stoneValue[i] - dp[i+1],
                stoneValue[i] + stoneValue[i+1] - dp[i+2],
                stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]
            )
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
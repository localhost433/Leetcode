class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = [0] * (n+1)
        dp = [[float('inf')] * (n+1) for _ in range(k+1)]
        for i in range(n):
            s[i+1] = s[i] + nums[i]
        dp[0][0] = 0
        for i in range(1, k+1):
            for j in range(1, n+1):
                for p in range(j):
                    cur = max(dp[i-1][p], s[j]-s[p])
                    dp[i][j] = min(dp[i][j], cur)
        return dp[k][n]

        
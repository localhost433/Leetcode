class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = 0
        for j in range(1, n):
            for i in range(j):
                if abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[j], dp[i]+1)
        return -1 if dp[-1] < 0 else dp[n-1]
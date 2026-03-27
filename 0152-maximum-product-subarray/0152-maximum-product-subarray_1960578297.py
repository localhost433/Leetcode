class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ret = nums[0]
        dp = [[0, 0] for _ in range(n)]
        dp[0][0], dp[0][1] = nums[0], nums[0]
        for i in range(1, n):
            option = (nums[i], nums[i] * dp[i-1][0], nums[i] * dp[i-1][1])
            dp[i][0] = max(option)
            dp[i][1] = min(option)
            ret = max(dp[i][0], ret)
        return ret
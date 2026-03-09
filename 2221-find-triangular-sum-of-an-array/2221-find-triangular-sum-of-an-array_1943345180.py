class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        c = 1
        ans = 0
        for i in range(n):
            ans += (c * nums[i]) % 10
            if i < n - 1:
                c = c * (n - 1 - i) // (i + 1)
            else:
                c = 0
        return ans % 10
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        cur = 0
        for i, num in enumerate(nums):
            cur += num * i
        best = cur
        for i in range(1, n):
            cur += s - n * nums[n-i]
            if cur > best:
                best = cur
        return best
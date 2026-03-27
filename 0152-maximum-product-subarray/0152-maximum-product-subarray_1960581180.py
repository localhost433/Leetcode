class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ret = nums[0]
        minp, maxp = nums[0], nums[0]
        for i in range(1, n):
            options = (nums[i], nums[i] * maxp, nums[i] * minp)
            maxp = max(options)
            minp = min(options)
            ret = max(maxp, ret)
        return ret
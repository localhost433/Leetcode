class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[0]
        ret = nums[0]
        for i in range(1, n):
            s = max(s + nums[i], nums[i])
            ret = max(s, ret)
        return ret
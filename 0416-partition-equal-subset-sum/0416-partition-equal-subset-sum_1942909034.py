class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        s >>= 1
        dp = 1
        for num in nums:
            dp |= dp << num
        return ((dp >> s) & 1) == 1
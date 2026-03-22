class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m, i = 0, 0
        while i < len(nums):
            if i > m:
                return False
            m = max(m, i + nums[i])
            i += 1
        return m >= len(nums) - 1
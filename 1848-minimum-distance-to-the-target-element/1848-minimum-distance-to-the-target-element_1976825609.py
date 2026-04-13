class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        for i in range(n):
            if start - i > -1 and nums[start - i] == target:
                return i
            if start + i < n and nums[start + i] == target:
                return i
        return -1
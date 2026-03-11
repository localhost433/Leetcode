class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        n = len(nums)
        for i in range(0, n-1, 2):
           s += min(nums[i], nums[i+1])
        return s
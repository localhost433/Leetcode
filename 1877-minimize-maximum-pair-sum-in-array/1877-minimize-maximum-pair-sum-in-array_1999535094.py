class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        s = 0
        for i in range(n//2):
            num = nums[n-i-1]
            s = max(nums[i] + num, s)
        return s
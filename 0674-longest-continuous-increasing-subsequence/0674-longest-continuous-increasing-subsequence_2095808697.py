class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        s = 1
        c = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                c += 1
            else:
                c = 1
            s = max(c, s)
        return s
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        s = 1
        c = 1
        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                c += 1
                s = max(c, s)
            else:
                c = 1
        return s
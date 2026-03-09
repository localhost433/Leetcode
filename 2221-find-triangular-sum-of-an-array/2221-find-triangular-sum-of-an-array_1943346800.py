class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        newNums = [0] * (n-1)
        for i in range(n-1):
            newNums[i] = (nums[i] + nums[i+1]) % 10
        return self.triangularSum(newNums)
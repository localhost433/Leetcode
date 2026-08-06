class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1] * n
        for i in range(1, n):
            ret[i] = ret[i-1] * nums[i-1]
        suf = 1
        for j in range(n-1, -1, -1):
            ret[j] *= suf
            suf *= nums[j]
        return ret
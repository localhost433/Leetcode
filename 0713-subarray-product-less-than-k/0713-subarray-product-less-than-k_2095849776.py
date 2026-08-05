class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        ret = 0
        prod = 1
        j = 0
        for i, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod //= nums[j]
                j += 1
            ret += (i - j + 1)
        return ret
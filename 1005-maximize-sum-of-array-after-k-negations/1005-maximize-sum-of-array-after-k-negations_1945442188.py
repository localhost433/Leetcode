class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        m = sum(nums)
        if k % 2 == 1:
            nums = sorted(nums)
            return m - 2 * nums[0]
        return m
        
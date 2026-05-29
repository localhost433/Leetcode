class Solution:
    def minElement(self, nums: List[int]) -> int:
        small = 10 ** 4
        for num in nums:
            cur = 0
            while num:
                cur += num % 10
                num //= 10
            small = min(small, cur)
        return small
                
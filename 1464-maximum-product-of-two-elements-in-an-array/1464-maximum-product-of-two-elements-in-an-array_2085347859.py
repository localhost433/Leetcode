class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, m = 0, 0
        for num in nums:
            if num >= m:
                n, m = m, num
            elif num > n:
                n = num
        return (n-1) * (m-1)
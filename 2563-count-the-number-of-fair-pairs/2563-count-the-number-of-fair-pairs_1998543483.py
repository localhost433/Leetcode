from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        def count(num: int) -> int:
            i, j = 0, n-1
            c = 0
            while i < j:
                if nums[i] + nums[j] < num:
                    c += j - i
                    i += 1
                else:
                    j -= 1
            return c
        return count(upper+1) - count(lower)
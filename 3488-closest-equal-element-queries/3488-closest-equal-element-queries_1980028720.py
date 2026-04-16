from bisect import bisect_left
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        m = defaultdict(list)
        for i, num in enumerate(nums):
            m[num].append(i)
            
        res = []
        for q in queries:
            target = nums[q]
            idx = m[target]
            if len(idx) <= 1:
                res.append(-1)
                continue
            
            pos = bisect_left(idx, q)
            left = idx[(pos - 1) % len(idx)]
            right = idx[(pos + 1) % len(idx)]
            d1 = abs(q - left)
            d2 = abs(q - right)
            res.append(min(d1, d2, n - d1, n - d2))
            
        return res
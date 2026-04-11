class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        locs = [[] for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            locs[num].append(i)
        d = float('inf')
        found = False
        for idx in locs:
            if len(idx) >= 3:
                found = True
                for i in range(2, len(idx)):
                    dist = 2 * (idx[i] - idx[i-2])
                    d = min(d, dist)
        return d if found else -1
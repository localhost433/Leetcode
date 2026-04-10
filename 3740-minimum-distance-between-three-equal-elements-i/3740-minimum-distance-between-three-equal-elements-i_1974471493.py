class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        locs = [[] for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            locs[num].append(i)
        d = float('inf')
        found = False
        for indices in locs:
            if len(indices) >= 3:
                found = True
                for i in range(2, len(indices)):
                    dist = 2*(indices[i] - indices[i-2])
                    d = min(d, dist)
        return d if found else -1
class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        dist = float('inf')
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                dist = min(dist, i - seen[num])
            seen[int(str(num)[::-1])] = i
        return dist if dist != float('inf') else -1
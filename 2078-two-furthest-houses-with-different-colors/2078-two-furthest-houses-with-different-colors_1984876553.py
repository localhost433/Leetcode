class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        dist = 0
        for i in range(n):
            for j in range(n-1, i, -1):
                if colors[i] != colors[j]:
                    dist = max(dist, abs(i-j))
        for j in range(n-1, i, -1):
            for i in range(n):
                if colors[i] != colors[j]:
                    dist = max(dist, abs(i-j))
        return dist
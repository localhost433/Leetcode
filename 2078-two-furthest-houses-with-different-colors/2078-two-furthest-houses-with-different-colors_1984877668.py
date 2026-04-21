class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = n - 1
        while colors[0] == colors[i]:
            i -= 1
        j = 0
        while colors[j] == colors[n-1]:
            j += 1
        return max(i, n-1-j)
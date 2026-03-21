class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        def diff(e: List[int]) -> int:
            u = sorted(set(e))
            if len(u) < 2:
                return 0
            d = float('inf')
            for i in range(1, len(u)):
                diff = u[i] - u[i-1]
                if diff < d:
                    d = diff
                if d == 1:
                    return 1
            return int(d)
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                sub = []
                for r in range(i, i + k):
                    sub.extend(grid[r][j : j + k])
                ans[i][j] = diff(sub)
        return ans
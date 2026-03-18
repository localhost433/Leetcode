class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                a = grid[i-1][j] if i > 0 else 0
                b = grid[i][j-1] if j > 0 else 0
                c = grid[i-1][j-1] if i > 0 and j > 0 else 0
                grid[i][j] += a + b - c
                if grid[i][j] <= k:
                    count += 1
                else:
                    break
        return count

# [[10,12],[14,15],[1,1],[3,90]]
# 44
# [[10,12,12,1,2],[14,15,45,76,3],[1,1,4,76,23],[3,90,87,54,876]]
# 248
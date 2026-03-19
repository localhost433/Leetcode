class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        count = 0
        n = len(grid)
        m = len(grid[0])
        x = [[0] * (m + 1) for _ in range(n + 1)]
        y = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                x[i+1][j+1] += x[i][j+1] + x[i+1][j] - x[i][j] + (1 if grid[i][j] == 'X' else 0)
                y[i+1][j+1] += y[i][j+1] + y[i+1][j] - y[i][j] + (1 if grid[i][j] == 'Y' else 0)
                if (x[i+1][j+1] > 0 and x[i+1][j+1] == y[i+1][j+1]):
                    count += 1
        return count
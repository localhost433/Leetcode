class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        count = 0
        col = [[0] * 2 for _ in range(m)]
        for row in grid:
            cur = 0
            x = 0
            for j in range(m):
                if row[j] == "X":
                    col[j][0] += 1
                    col[j][1] += 1
                elif row[j] == "Y":
                    col[j][0] -= 1
                cur += col[j][0]
                x += col[j][1]
                if cur == 0 and x > 0:
                    count += 1
        return count
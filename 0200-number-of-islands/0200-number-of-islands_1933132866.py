class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        islands = 0
        def dfs(r: int, c: int):
            visited.add((r, c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    grid[nr][nc] == '1' and
                    (nr, nc) not in visited
                ):
                    dfs(nr, nc)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)
        return islands
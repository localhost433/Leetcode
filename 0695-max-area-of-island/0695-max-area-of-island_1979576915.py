class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        def bfs(r, c) -> int:
            area = 0
            queue = deque([(r, c)])
            grid[r][c] = 0
            while queue:
                r, c = queue.popleft()
                area += 1
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1):
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            return area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret = max(ret, bfs(i, j))
        return ret
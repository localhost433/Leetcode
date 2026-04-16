class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac_q = deque()
        atl_q = deque()
        for r in range(m):
            pac_q.append((r, 0))
            atl_q.append((r, n - 1))
        for c in range(n):
            pac_q.append((0, c))
            atl_q.append((m - 1, c))

        def get_reachable(queue) -> set():
            reachable = set()
            while queue:
                r, c = queue.popleft()
                if (r, c) in reachable:
                    continue
                reachable.add((r, c))
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]:
                        if (nr, nc) not in reachable:
                            queue.append((nr, nc))
            return reachable

        pac_reachable = get_reachable(pac_q)
        atl_reachable = get_reachable(atl_q)
        return [list(coord) for coord in pac_reachable.intersection(atl_reachable)]

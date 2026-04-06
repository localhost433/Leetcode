class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ob_set = {tuple(obs) for obs in obstacles}
        x, y = 0, 0
        d = 0
        maxd = 0
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]
                for _ in range(c):
                    if (x + dx, y + dy) in ob_set:
                        break
                    x += dx
                    y += dy
                maxd = max(maxd, x * x + y * y)
        return maxd
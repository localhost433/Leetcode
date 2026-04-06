class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if len(commands) == 0:
            return 0
        cur = [0, 0]
        d = 0
        ob_set = {tuple(obs) for obs in obstacles}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        maxd = 0
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                for _ in range(c):
                    nx, ny = cur[0] + directions[d][0], cur[1] + directions[d][1]
                    if (nx, ny) in ob_set:
                        break
                    cur = [nx, ny]
                    maxd = max(maxd, cur[0]**2 + cur[1]**2)
        return maxd

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        ret = [[0] * m for _ in range(n)]

        cur = 1
        for i in range(n):
            for j in range(m):
                ret[i][j] = cur
                cur = (cur * grid[i][j]) % MOD

        cur = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                ret[i][j] = (ret[i][j] * cur) % MOD
                cur = (cur * grid[i][j]) % MOD
        return ret
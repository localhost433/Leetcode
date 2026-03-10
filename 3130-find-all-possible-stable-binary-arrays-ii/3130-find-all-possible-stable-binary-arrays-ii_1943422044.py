class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        Z, O, L = zero, one, limit
        dp0 = [[0] * (O + 1) for _ in range(Z + 1)]
        dp1 = [[0] * (O + 1) for _ in range(Z + 1)]

        for i in range(1, min(L, Z) + 1):
            dp0[i][0] = 1
        for j in range(1, min(L, O) + 1):
            dp1[0][j] = 1

        for i in range(0, Z + 1):
            for j in range(0, O + 1):
                if i == 0 or j == 0:
                    continue

                add0 = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                sub0 = dp1[i - L - 1][j] if (i - L - 1) >= 0 else 0
                dp0[i][j] = (add0 - sub0) % MOD

                add1 = (dp0[i][j-1] + dp1[i][j-1]) % MOD
                sub1 = dp0[i][j - L - 1] if (j - L - 1) >= 0 else 0
                dp1[i][j] = (add1 - sub1) % MOD

        return (dp0[Z][O] + dp1[Z][O]) % MOD
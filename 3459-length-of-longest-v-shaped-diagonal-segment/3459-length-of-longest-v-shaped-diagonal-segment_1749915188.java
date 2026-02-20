class Solution {
    int[] DR = {-1, +1, +1, -1};
    int[] DC = {+1, +1, -1, -1};

    public int lenOfVDiagonal(int[][] grid) {
        int R = grid.length, C = grid[0].length;
        int[][][] dp2 = new int[4][R][C];
        int[][][] dp0 = new int[4][R][C];

        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                fillCell(grid, dp2, dp0, 0, r, c, R, C);
                fillCell(grid, dp2, dp0, 3, r, c, R, C);
            }
        }

        for (int r = R - 1; r >= 0; --r) {
            for (int c = 0; c < C; ++c) {
                fillCell(grid, dp2, dp0, 1, r, c, R, C);
                fillCell(grid, dp2, dp0, 2, r, c, R, C);
            }
        }

        int ans = 0;

        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (grid[r][c] != 1) continue;

                for (int a = 0; a < 4; ++a) {
                    int b = (a + 1) % 4;
                    int Ar = r + DR[a], Ac = c + DC[a];
                    int L1 = inBounds(Ar,Ac,R,C) ? dp2[a][Ar][Ac] : 0;
                    int best = 0;
                    int pr = r, pc = c;
                    for (int x = 0; x <= L1; ++x) {
                        int Br = pr + DR[b], Bc = pc + DC[b];
                        if (inBounds(Br,Bc,R,C)) {
                        int cont = (x % 2 == 0) ? dp2[b][Br][Bc] : dp0[b][Br][Bc];
                        best = Math.max(best, x + cont);
                        }
                        pr += DR[a]; pc += DC[a];
                    }
                    ans = Math.max(ans, 1 + best);
                }
            }
        }
        return ans;
    }
    public void fillCell(int[][] grid, int[][][] dp2, int[][][] dp0, int d, int r, int c, int R, int C) {
        int nr = r + DR[d], nc = c + DC[d];
        int next2 = inBounds(nr, nc, R, C) ? dp2[d][nr][nc] : 0;
        int next0 = inBounds(nr, nc, R, C) ? dp0[d][nr][nc] : 0;

        dp2[d][r][c] = (grid[r][c] == 2) ? 1 + next0 : 0;
        dp0[d][r][c] = (grid[r][c] == 0) ? 1 + next2 : 0;
    }

    public boolean inBounds(int r, int c, int R, int C) {
        return 0 <= r && r < R && 0 <= c && c < C;
    }
}
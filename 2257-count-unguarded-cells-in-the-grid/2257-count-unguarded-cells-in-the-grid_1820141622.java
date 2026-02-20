import java.util.*;

class Solution {
    private static final byte WALL  = 1 << 0;  // 0001
    private static final byte GUARD = 1 << 1;  // 0010
    private static final byte HSEEN = 1 << 2;  // 0100
    private static final byte VSEEN = 1 << 3;  // 1000

    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        final int N = m * n;
        byte[] grid = new byte[N];

        for (int[] w : walls) grid[w[0] * n + w[1]] |= WALL;
        for (int[] g : guards) grid[g[0] * n + g[1]] |= GUARD;

        for (int i = 0; i < m; i++) {
            int rowBase = i * n;

            boolean visL = false, visR = false;
            for (int off = 0; off < n; off++) {
                int jL = rowBase + off;
                int jR = rowBase + (n - 1 - off);

                byte cL = grid[jL];
                if ((cL & WALL) != 0) { visL = false; }
                else if ((cL & GUARD) != 0) { visL = true; }
                else if (visL) { grid[jL] |= HSEEN; }

                byte cR = grid[jR];
                if ((cR & WALL) != 0) { visR = false; }
                else if ((cR & GUARD) != 0) { visR = true; }
                else if (visR) { grid[jR] |= HSEEN; }
            }
        }

        for (int j = 0; j < n; j++) {
            boolean visT = false, visB = false;
            for (int off = 0; off < m; off++) {
                int iT = off;
                int iB = m - 1 - off;

                int idxT = iT * n + j, idxB = iB * n + j;

                byte cT = grid[idxT];
                if ((cT & WALL) != 0) { visT = false; }
                else if ((cT & GUARD) != 0) { visT = true; }
                else if (visT) { grid[idxT] |= VSEEN; }

                byte cB = grid[idxB];
                if ((cB & WALL) != 0) { visB = false; }
                else if ((cB & GUARD) != 0) { visB = true; }
                else if (visB) { grid[idxB] |= VSEEN; }
            }
        }

        int count = 0;
        for (int idx = 0; idx < N; idx++) {
            byte c = grid[idx];
            if ((c & (WALL | GUARD | HSEEN | VSEEN)) == 0) count++;
        }
        return count;
    }
}

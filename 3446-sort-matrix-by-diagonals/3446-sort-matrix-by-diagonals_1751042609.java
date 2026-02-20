import java.util.Arrays;

class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int n = grid.length;
        if (n <= 1) return grid;

        int diags = 2 * n - 1;
        int[][] buckets = new int[diags][];

        for (int D = 0; D < diags; D++) {
            buckets[D] = new int[n - Math.abs(D - (n - 1))];
        }

        int[] ptr = new int[diags];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int D = (i - j) + (n - 1);
                buckets[D][ptr[D]++] = grid[i][j];
            }
        }

        for (int D = 0; D < diags; D++) {
            Arrays.sort(buckets[D]);
        }

        for (int D = 0; D < diags; D++) {
            int d  = D - (n - 1);
            int i0 = Math.max(0, d);
            int j0 = -Math.min(0, d);
            int L  = buckets[D].length;

            if (D < n - 1) {
                for (int t = 0; t < L; t++) {
                    grid[i0 + t][j0 + t] = buckets[D][t];
                }
            } else {
                for (int t = 0; t < L; t++) {
                    grid[i0 + t][j0 + t] = buckets[D][L - 1 - t];
                }
            }
        }
        return grid;
    }
}

class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        if (m == 0) return new int[0];
        int[] ret = new int[m * n];
        int p = 0;
        for (int d = 0; d < m+n-1; d++) {
            int r0 = Math.max(0, d - (n - 1));
            int r1 = Math.min(d, m - 1);
            if (d % 2 == 0) {
                for (int r = r1; r >= r0; --r) {
                    int c = d - r;
                    ret[p++] = mat[r][c];
                }
            } else {
                for (int r = r0; r <= r1; ++r) {
                    int c = d - r;
                    ret[p++] = mat[r][c];
                }
            }
        }
        return ret;
    }
}
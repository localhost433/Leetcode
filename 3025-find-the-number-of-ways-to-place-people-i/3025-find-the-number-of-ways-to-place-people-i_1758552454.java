import java.util.*;

class Solution {
    private boolean emptyClosedRect(int i, int j, int[][] pts) {
        int[] a = pts[i];
        int[] b = pts[j];
        if (!(a[0] <= b[0] && a[1] >= b[1] && (a[0] < b[0] || a[1] > b[1]))) return false;
        for (int k = 0; k < pts.length; ++k) {
            if (k == i || k == j) continue;
            int[] p = pts[k];
            if (a[0] <= p[0] && p[0] <= b[0] &&
                b[1] <= p[1] && p[1] <= a[1])
                return false;
        }
        return true;
    }

    public int numberOfPairs(int[][] points) {
        int n = points.length, ans = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                if (emptyClosedRect(i, j, points)) ++ans;
            }
        return ans;
    }
}

import java.util.*;

class Solution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points, Comparator
            .comparingInt((int[] p) -> p[0])
            .thenComparingInt(p -> -p[1]));

        int n = points.length, ans = 0;
        for (int i = 0; i < n; ++i) {
            int yi = points[i][1];
            int maxY = Integer.MIN_VALUE;
            for (int j = i + 1; j < n; ++j) {
                int yj = points[j][1];
                if (yi >= yj && yj > maxY) {
                    ++ans;
                    maxY = yj;
                }
            }
        }
        return ans;
    }
}
class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(b[0], a[0]);
        });
        int p = -1, q = -1;
        int count = 0;
        for (int[] interval: intervals) {
            int l = interval[0];
            int r = interval[1];
            if (l <= p) {
                continue;
            }
            else if (l <= q) {
                count++;
                p = q;
                q = r;
            } else {
                count += 2;
                q = r;
                p = q - 1;
            }
        }
        return count;
    }
}
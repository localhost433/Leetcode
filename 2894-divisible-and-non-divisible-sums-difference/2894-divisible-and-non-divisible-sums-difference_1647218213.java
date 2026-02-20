class Solution {
    public int differenceOfSums(int n, int m) {
        boolean larger = n > m;
        int sum = (1 + n) * n / 2;
        if (m == 1) {
            return -sum;
        } else if (!larger) {
            if (n == m) {
                return sum - 2 * m;
            }
            return sum;
        }
        for (int i = n; i > 0; i--) {
            if (i % m == 0) {
                int num2 = (m + i) * (i / m) / 2;
                return sum - 2 * num2;
            }
        }
        return sum;
    }
}
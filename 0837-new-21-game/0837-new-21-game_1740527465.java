class Solution {
    public double new21Game(int n, int k, int maxPts) {
        if ((k == 0) || n >= k - 1 + maxPts) {
            return 1D;
        }
        double[] dp = new double[n + 1];
        for (int s = k; s <= n; ++s) {
            dp[s] = 1D;
        }
        double window = Math.min(n - k + 1, maxPts);
        dp[k - 1] = window / maxPts;
        for (int s = k - 2; s >= 0; --s) {
            double out = (s + 1 + maxPts <= n) ? dp[s + 1 + maxPts] : 0.0;
            window = window + dp[s + 1] - out;
            dp[s] = window / maxPts;
        }
        return dp[0];
    }
}
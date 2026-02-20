class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        
        for (String s : strs) {
            int z = 0, o = 0;
            for (char c : s.toCharArray()) {
                if (c == 48) z++;
                else o++;
            }   
            for (int a = m; a >= z; a--) {
                for (int b = n; b >= o; b--) {
                    dp[a][b] = Math.max(dp[a][b], 1 + dp[a - z][b - o]);
                }
            }
        }
        return dp[m][n];
    }
}

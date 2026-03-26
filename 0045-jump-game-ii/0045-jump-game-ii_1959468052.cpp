class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, n + 1);
        dp[n - 1] = 0;
        for (int i = n - 2; i > -1; --i) {
            int max_jump = std::min(i + nums[i], n - 1);
            for (int j = i + 1; j <= max_jump; ++j) {
                dp[i] = std::min(dp[i], 1 + dp[j]);
            }
        }
        return dp[0];
    }
};
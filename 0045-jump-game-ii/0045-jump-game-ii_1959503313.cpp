class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            nums[i] = max(nums[i] + i, nums[i-1]);
        }
        int idx = 0;
        int ret = 0;
        while (idx < n - 1) {
            ret++;
            idx = nums[idx];
        }
        return ret;
    }
};
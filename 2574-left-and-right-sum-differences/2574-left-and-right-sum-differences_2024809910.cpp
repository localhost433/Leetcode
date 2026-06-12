using namespace std;

class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = size(nums);
        vector<int> ans(n);
        int p = 0, s = 0;
        for (int i = 0; i < n; i++) {
            ans[i] = p;
            p += nums[i];
        }
        for (int j = n-1; j > -1; j--) {
            ans[j] = abs(ans[j] - s);
            s += nums[j];
        }
        return ans;
    }
};
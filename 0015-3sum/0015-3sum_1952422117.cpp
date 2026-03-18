class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> ret;
        int n = nums.size();
        
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < n; ++i) {
            if (nums[0] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    ret.push_back({nums[i], nums[l], nums[r]});

                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;
                    
                    l++;
                    r--;
                }
            }
        }
        return ret;
    }
};
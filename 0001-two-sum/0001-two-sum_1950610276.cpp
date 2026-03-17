class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> idx;
        for (int i = 0; i < nums.size(); ++i) {
            int c = target - nums[i];
            if (idx.find(c) != idx.end()) {
                return {idx[c], i};
            } idx[nums[i]] = i;
        } return {};
    }
};
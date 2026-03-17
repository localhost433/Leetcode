class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int x: nums) {
            if (seen.count(x)) {
                return true;
            } seen.insert(x);
        } return false;
    }
};
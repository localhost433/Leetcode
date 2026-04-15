class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        std::sort(pairs.begin(), pairs.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int longest = 0;
        long long end = -2e9;
        for (const auto& pair : pairs) {
            if (pair[0] > end) {
                longest++;
                end = pair[1];
            }
        }
        return longest;
    }
};
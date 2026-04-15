class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size();
        int longest = 1;
        vector<int>length(n, 1);
        std::sort(pairs.begin(), pairs.end());
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (pairs[i][0] > pairs[j][1]) {
                    length[i] = max(length[j] + 1, length[i]);
                    longest = max(longest, length[i]);
                }
            }
        }
        return longest;
    }
};
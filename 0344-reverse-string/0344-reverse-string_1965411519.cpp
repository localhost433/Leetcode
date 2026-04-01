class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0;
        int n = s.size();
        while (i < n / 2) {
            int tmp = s[i];
            s[i] = s[n-i-1];
            s[n-i-1] = tmp;
            i++;
        }
    }
};
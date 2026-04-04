class Solution {
public:
    std::string reverseWords(std::string s) {
        std::reverse(s.begin(), s.end());
        int n = s.size();
        int i = 0;
        int j = 0;
        while (i < n) {
            while (i < n && s[i] == ' ') {
                i++;
            }
            if (i >= n) break;
            if (j > 0) {
                s[j++] = ' ';
            }
            int start = j;
            while (i < n && s[i] != ' ') {
                s[j++] = s[i++];
            }
            std::reverse(s.begin() + start, s.begin() + j);
        }
        s.resize(j);
        return s;
    }
};
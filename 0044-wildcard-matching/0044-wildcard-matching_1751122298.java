class Solution {
    public boolean isMatch(String s, String p) {
        int n = s.length(), m = p.length();
        int i = 0, j = 0;
        int star = -1;
        int iAfterStar = -1;

        while (i < n) {
            if (j < m && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i))) {
                i++;
                j++;
            }
            else if (j < m && p.charAt(j) == '*') {
                star = j;
                iAfterStar = i;
                while (j < m && p.charAt(j) == '*') j++;
            }
            else if (star != -1) {
                iAfterStar++;
                i = iAfterStar;
                j = star + 1;
            }
            else {
                return false;
            }
        }
        while (j < m && p.charAt(j) == '*') j++;
        return j == m;
    }
}

class Solution {
    public String largestGoodInteger(String num) {
        char best = 0;
        boolean f = false;
        int n = num.length();
        for (int i = 0; i + 2 < n; i++) {
            char c = num.charAt(i);
            if (c == num.charAt(i + 1) && c == num.charAt(i + 2)) {
                if (!f || c > best) {
                    best = c;
                    f = true;
                }
            }
        }
        if (!f) return "";
        return String.valueOf(best).repeat(3);
    }
}
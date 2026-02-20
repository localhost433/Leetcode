class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] last = new int[128];
        for (int i = 0; i < 128; i++) {
            last[i] = -1;
        }
        int left = 0, max = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            if (last[c] >= left) {
                left = last[c] + 1;
            }
            last[c] = r;
            max = Math.max(max, r - left + 1);
        }
        return max;
    }
}
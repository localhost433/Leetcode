class Solution {
    public int minCost(String colors, int[] neededTime) {
        int n = colors.length();
        int total = 0;
        int keep = neededTime[0];
        for (int i = 1; i < n; i++) {
            if (colors.charAt(i) == colors.charAt(i - 1)) {
                total += Math.min(keep, neededTime[i]);
                keep = Math.max(keep, neededTime[i]);
            } else keep = neededTime[i];
        }
        return total;
    }
}

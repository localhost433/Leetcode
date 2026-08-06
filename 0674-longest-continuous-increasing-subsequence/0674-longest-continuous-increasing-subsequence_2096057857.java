class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int n = nums.length;
        if (n < 2) {
            return 1;
        }
        int cur = 1;
        int max = 1;
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i-1]) {
                cur++;
            } else {
                cur = 1;
            }
            max = Math.max(max, cur);
        }
        return max;
    }
}
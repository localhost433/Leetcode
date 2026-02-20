class Solution {
        public int findLHS(int[] nums) {
        if (nums.length < 2) return 0;
        Arrays.sort(nums);
        int prevVal   = Integer.MIN_VALUE;
        int prevCount = 0;
        int currVal   = nums[0];
        int currCount = 1;
        
        int best = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == currVal) {
                currCount++;
            } else {
                if (currVal == prevVal + 1) {
                    best = Math.max(best, prevCount + currCount);
                }
                prevVal   = currVal;
                prevCount = currCount;
                currVal   = nums[i];
                currCount = 1;
            }
        }
        if (currVal == prevVal + 1) {
            best = Math.max(best, prevCount + currCount);
        }
        return best;
    }
}
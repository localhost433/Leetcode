class Solution {
    public long countConsec(int n) {
        return (long) n * (n + 1) / 2;
    }

    public long zeroFilledSubarray(int[] nums) {
        int consec = 0;
        long count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                consec++;
            } else {
                count += countConsec(consec);
                consec = 0;
            }
        }
        count += countConsec(consec);
        return count;
    }
}
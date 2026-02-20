class Solution {
    public int maxFrequencyElements(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        
        int vmax = 0;
        for (int x : nums) vmax = Math.max(vmax, x);
        int[] table = new int[vmax + 1];

        for (int i = 0; i < n; i++) {
            table[nums[i]]++;
        }
        
        int max = 0, count = 0;
        for (int j = 0; j < table.length; j++) {
            int f = table[j];
            if (f > max) {
                max = f;
                count = 1;
            } else if (f == max && f > 0) {
                count++;
            }
        }
        return max * count;
    }
}
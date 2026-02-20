class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        int[] count = new int[value];

        for (int x : nums) {
            int r = x % value;
            if (r < 0) r += value;
            count[r]++;
        }

        int m = 0;
        while (true) {
            int r = m % value;
            if (count[r] == 0) return m;
            count[r]--;
            m++;
        }
    }
}

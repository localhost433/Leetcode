class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        if (k == 1) return true;
        int n = nums.size();
        if (n < 2 * k) return false;
        for (int i = 0; i <= n - 2 * k; i++) {
            if (increasing(nums, i, i + k) && increasing(nums, i + k, i + 2 * k)) return true;
        }
        return false;
    }

    public boolean increasing(List<Integer> a, int l, int r) {
        for (int i = l + 1; i < r; i++) {
            if (a.get(i) <= a.get(i - 1)) return false;
        }
        return true;
    }
}
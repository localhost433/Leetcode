class Solution {
    public int smallestRepunitDivByK(int k) {
        if (k % 5 == 0 || k % 2 == 0) return -1;
        int rem = 0;
        int n = 1;
        while (n <= k) {
            rem = (rem * 10 + 1) % k;
            n++;
            if (rem == 0) return n - 1;
        }
        return -1;
    }
}
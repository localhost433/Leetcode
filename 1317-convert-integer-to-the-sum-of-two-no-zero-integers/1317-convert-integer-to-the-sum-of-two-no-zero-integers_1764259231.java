class Solution {
    public boolean valid(int n) {
        while (n != 0) {
            if (n % 10 == 0) return false;
            n /= 10;
        }
        return true;
    }
    
    public int[] getNoZeroIntegers(int n) {
        int[] ret = new int[2];
        for (int i = 1; i < n; i++) {
            if ((valid(i)) && (valid(n-i))) {
                ret[0] = i;
                ret[1] = n - i;
                return ret;
            }
        }
        return ret;
    }
}
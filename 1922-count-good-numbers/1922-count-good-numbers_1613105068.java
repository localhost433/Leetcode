class Solution {
    private final int mod = 1000000007;

    public int countGoodNumbers(long n) {
        long evenP = (n + 1) / 2;
        long oddP = n / 2;

        long even = modPow(5, evenP, mod);
        long odd = modPow(4, oddP, mod);

        return (int) (even * odd % mod);
    }

    private long modPow(long base, long exp, int mod) {
        long result = 1;
        base %= mod;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }

        return result;
    }
}

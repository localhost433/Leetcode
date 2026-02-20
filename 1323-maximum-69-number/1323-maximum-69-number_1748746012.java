class Solution {
    public int maximum69Number (int num) {
        int add = 0, place = 1, best = 0, n = num;
        while (n > 0) {
            if ((n % 10) == 6) best = place;
            n /= 10;
            place *= 10;
        }
        add = (best == 0) ? 0 : 3 * best;
        return num + add;
    }
}
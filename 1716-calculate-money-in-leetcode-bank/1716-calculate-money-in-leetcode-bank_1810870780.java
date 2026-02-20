class Solution {
    public int totalMoney(int n) {
        int r = n % 7;
        return (n*(n + 49) + (6*(r-7))*r) / 14;
    }
}
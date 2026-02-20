class Solution {
    public int makeTheIntegerZero(int num1, int num2){
        for (int i = 0; i < 61; i++) {
            long target = num1 - (long) i * num2;
            if (target < i) return -1;
            if (i >= Long.bitCount(target)) return i;
        }
        return -1;
    }
}
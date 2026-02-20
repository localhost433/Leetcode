class Solution {
    public int findLucky(int[] arr) {
        int[] f = new int[501];
        for (int i = 0; i < arr.length; i++) {
            f[arr[i]]++;
        }
        int s = -1;
        for (int j = 1; j < 501; j++) {
            if (f[j] == j) {
                s = j;
            }
        }
        return s;
    }
}
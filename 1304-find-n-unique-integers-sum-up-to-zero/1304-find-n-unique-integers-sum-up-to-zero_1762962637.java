class Solution {
    public int[] sumZero(int n) {
        int[] arr = new int[n];
        if (n == 1) return new int[1];
        int c = -n/2;
        for (int i = 0 ; i < n; i++) {
            if ((n % 2 == 0) && (c == 0)) {
                c++;
            }
            arr[i] = c++;
        }
        return arr;
    }
}
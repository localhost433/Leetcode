class Solution {
    public int numberOfBeams(String[] bank) {
        int m = bank.length;
        int n = bank[0].length();
        int[] counts = new int[m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (bank[i].charAt(j) == '1') {
                    counts[i]++;
                }
            }
        }
        int nums = 0, inc = 0;
        for (int curRow = 0; curRow < m; curRow++) {
            int count = counts[curRow];
            if (count == 0) continue;
            if (count != 0) nums += inc * count;
            inc = count;
        }
        return nums;
    }
}
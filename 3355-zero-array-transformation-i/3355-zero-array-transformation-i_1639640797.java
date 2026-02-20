import java.util.Arrays;

class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] diff = new int[n+1];
        
        for (int[] qr : queries) {
            int l = qr[0], r = qr[1];
            diff[l]++;          
            if (r + 1 < n) 
                diff[r+1]--;
        }
        
        int cover = 0;
        for (int i = 0; i < n; i++) {
            cover += diff[i];
            if (cover < nums[i]) 
                return false;
        }
        return true;
    }
}
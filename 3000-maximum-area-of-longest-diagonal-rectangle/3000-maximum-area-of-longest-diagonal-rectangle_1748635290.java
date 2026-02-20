class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int maxSqDiag = 0;
        int maxArea = 0;
        
        for (int[] rect : dimensions) {
            int a = rect[0], b = rect[1];
            int sqDiag = a * a + b * b;
            int area = a * b;
            
            if (sqDiag > maxSqDiag) {
                maxSqDiag = sqDiag;
                maxArea = area;
            } else if (sqDiag == maxSqDiag && area > maxArea) {
                maxArea = area;
            }
        }
        
        return maxArea;
    }
}
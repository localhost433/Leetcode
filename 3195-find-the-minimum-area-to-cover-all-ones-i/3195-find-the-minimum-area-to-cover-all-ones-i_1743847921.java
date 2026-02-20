class Solution {
    public int minimumArea(int[][] grid) {
        int minx = grid[0].length, maxx = -1;
        int miny = grid.length, maxy = -1;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    minx = Math.min(minx, j);
                    miny = Math.min(miny, i);
                    maxx = Math.max(maxx, j);
                    maxy = Math.max(maxy, i);
                }
            }
        }
        return (maxx - minx + 1) * (maxy - miny + 1);
    }
}
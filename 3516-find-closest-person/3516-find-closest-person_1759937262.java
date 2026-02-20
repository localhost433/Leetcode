class Solution {
    public int findClosest(int x, int y, int z) {
        int distX = Math.abs(x - z);
        int distY = Math.abs(y - z);
        if (distX > distY) return 2;
        else if ((distX < distY)) return 1;
        else return 0;
    }
}
class Solution {
    public boolean judgeCircle(String moves) {
        int r = 0, u = 0;
        for (char move: moves.toCharArray()) {
            switch (move) {
                case 'L':
                    r--;
                    break;
                case 'R':
                    r++;
                    break;
                case 'U':
                    u++;
                    break;
                case 'D':
                    u--;
                    break;
            }
        } return r == 0 && u == 0;
    }
}
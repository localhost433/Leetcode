class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] row = new int[9];
        int[] col = new int[9];
        int[] box = new int[9];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char ch = board[r][c];
                if (ch == '.') continue;
                int d = ch - '0';
                int bit = 1 << (d - 1);
                int b = (r / 3) * 3 + (c / 3);
                if ((row[r] & bit) != 0) return false;
                if ((col[c] & bit) != 0) return false;
                if ((box[b] & bit) != 0) return false;
                row[r] |= bit;
                col[c] |= bit;
                box[b] |= bit;
            }
        }
        return true;
    }
}

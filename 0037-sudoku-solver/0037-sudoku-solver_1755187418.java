class Solution {
    private final int[] row = new int[9];
    private final int[] col = new int[9];
    private final int[] box = new int[9];
    private char[][] board;
    private int[] blanks;
    private int nBlanks;

    public void solveSudoku(char[][] board) {
        this.board = board;
        for (int i = 0; i < 9; i++) {
            row[i] = 0;
            col[i] = 0;
            box[i] = 0;
        }
        blanks = new int[81];
        nBlanks = 0;
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char ch = board[r][c];
                if (ch == '.') {
                    blanks[nBlanks] = r * 9 + c;
                    nBlanks = nBlanks + 1;
                } else {
                    int d = ((int) ch) - ((int) '0'); // 1..9
                    int bit = 1 << (d - 1);
                    int b = (r / 3) * 3 + (c / 3);
                    row[r] = row[r] | bit;
                    col[c] = col[c] | bit;
                    box[b] = box[b] | bit;
                }
            }
        }
        dfs(0);
    }

    private boolean dfs(int pos) {
        if (pos == nBlanks) {
            return true;
        }
        int best = pos;
        int minCnt = 10;
        for (int i = pos; i < nBlanks; i++) {
            int rc = blanks[i];
            int r = rc / 9;
            int c = rc % 9;
            int b = (r / 3) * 3 + (c / 3);
            int used = row[r] | col[c] | box[b];
            int cand = (~used) & 0x1FF;
            int cnt = countBits(cand);
            if (cnt < minCnt) {
                minCnt = cnt;
                best = i;
                if (cnt == 1) {
                    break;
                }
            }
        }
        if (minCnt == 0) {
            return false;
        }
        swap(blanks, pos, best);

        int rc = blanks[pos];
        int r = rc / 9;
        int c = rc % 9;
        int b = (r / 3) * 3 + (c / 3);
        int used = row[r] | col[c] | box[b];
        int cand = (~used) & 0x1FF;
        for (int d = 1; d <= 9; d++) {
            int bit = 1 << (d - 1);
            if ((cand & bit) == 0) {
                continue;
            }
            board[r][c] = (char) (((int) '0') + d);
            row[r] = row[r] | bit;
            col[c] = col[c] | bit;
            box[b] = box[b] | bit;
            if (dfs(pos + 1)) {
                return true;
            }
            row[r] = row[r] & (~bit);
            col[c] = col[c] & (~bit);
            box[b] = box[b] & (~bit);
            board[r][c] = '.';
        }
        swap(blanks, pos, best);
        return false;
    }

    private static void swap(int[] a, int i, int j) {
        if (i == j) {
            return;
        }
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }

    private static int countBits(int x) {
        int cnt = 0;
        for (int k = 0; k < 9; k++) {
            int mask = 1 << k;
            if ((x & mask) != 0) {
                cnt = cnt + 1;
            }
        }
        return cnt;
    }
}

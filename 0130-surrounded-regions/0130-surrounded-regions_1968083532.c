void dfs(char** board, int boardSize, int boardColSize, int r, int c) {
    if (r < 0 ||
        c < 0 ||
        r >= boardSize ||
        c >= boardColSize ||
        board[r][c] != 'O') {
        return;
}
    board[r][c] = 'T';
    dfs(board, boardSize, boardColSize, r + 1, c);
    dfs(board, boardSize, boardColSize, r - 1, c);
    dfs(board, boardSize, boardColSize, r, c + 1);
    dfs(board, boardSize, boardColSize, r, c - 1);
}

void solve(char** board, int boardSize, int* boardColSize) {
    int cols = boardColSize[0]; 
    for (int i = 0; i < boardSize; i++) {
        if (board[i][0] == 'O') {
            dfs(board, boardSize, cols, i, 0);
        }
        if (board[i][cols - 1] == 'O') {
            dfs(board, boardSize, cols, i, cols - 1);
        }
    }

    for (int j = 0; j < cols; j++) {
        if (board[0][j] == 'O') {
            dfs(board, boardSize, cols, 0, j);
        }
        if (board[boardSize - 1][j] == 'O') {
            dfs(board, boardSize, cols, boardSize - 1, j);
        }
    }

    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < cols; j++) {
            if (board[i][j] == 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] == 'T') {
                board[i][j] = 'O';
            }
        }
    }
}
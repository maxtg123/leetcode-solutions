class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }
    
    // Function to solve the Sudoku puzzle using backtracking
    private boolean solve(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                // If the cell is empty, try to fill it with a valid number
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) {
                        if (isValid(board, i, j, c)) {
                            board[i][j] = c;  // Try this number
                            if (solve(board)) {
                                return true;  // Continue solving recursively
                            }
                            board[i][j] = '.';  // Backtrack if no solution found
                        }
                    }
                    return false;  // If no valid number can be placed, return false
                }
            }
        }
        return true;  // If all cells are filled correctly
    }

    // Function to check if placing a number is valid
    private boolean isValid(char[][] board, int row, int col, char c) {
        // Check row
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == c) {
                return false;
            }
        }
        
        // Check column
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == c) {
                return false;
            }
        }
        
        // Check 3x3 grid
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                if (board[i][j] == c) {
                    return false;
                }
            }
        }
        
        return true;  // Valid placement
    }
}

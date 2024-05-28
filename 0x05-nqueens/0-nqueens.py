#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, N):
    # base case: If all queens are placed then return true
    if col >= N:
        return True

    # Consider this column and try placing the queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_n_queens(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen from board[i][col]
            board[i][col] = 0

    # If queen can not be place in any row in this column col then return false
    return False

def solve(N):
    # Initialize a N x N board with all cells as 0
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens(board, 0, N):
        print("No solution exists", file=sys.stderr)
        sys.exit(1)

    # Print the solution
    for row in board:
        line = [str(i) for i in row]
        print(" ".join(line))

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    N = sys.argv[1]

    if not N.isdigit():
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    solve(N)

if __name__ == "__main__":
    main()

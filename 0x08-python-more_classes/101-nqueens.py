#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper left diagonal
    zipped = zip(range(row, -1, -1), range(col, -1, -1))
    for i, j in zip:
        if board[i][j] == "Q":
            return (False)

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == "Q":
            return (False)

    return True


def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def backtrack(board, row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = "Q"
                backtrack(board, row + 1)
                board[row][col] = '.'

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)

#!/usr/bin/python3
import sys

"""Solves the N queens problem"""


def is_safe(board, row, col):
    """
    Checks if a queen can be placed in a certain position
    Args:
        board: 2D array
        row: row
        col: column
    Returns:
        True if queen can be placed
        False if queen cannot be placed
    Example:
        >>> board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        row = 0
        col = 0
        is_safe(board, row, col)
        True
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N, board, col):
    """
    Solves the N queens problem
    Args:
        N: size of the board
        board: 2D array
        col: column
    Example:
        >>> N = 4
        board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        col = 0
        solve_nqueens(N, board, col)
        [[0, 2], [1, 0], [2, 3], [3, 1]]
        [[0, 1], [1, 3], [2, 0], [3, 2]]
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            solve_nqueens(N, board, col + 1)

            board[i][col] = 0


def validate_input(args):
    """
    Validates input
    Args:
        args: command line arguments
    Returns:
        N: size of the board
    """
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def main():
    """
    Main function
    Example:
        >>> N = 4
        board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        col = 0
        solve_nqueens(N, board, col)
        [[0, 2], [1, 0], [2, 3], [3, 1]]
        [[0, 1], [1, 3], [2, 0], [3, 2]]
    """
    N = validate_input(sys.argv)

    board = [[0] * N for _ in range(N)]

    solve_nqueens(N, board, 0)


if __name__ == "__main__":
    main()

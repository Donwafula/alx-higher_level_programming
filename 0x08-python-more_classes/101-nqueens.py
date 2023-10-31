#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def init_board(n):
    """Initialize an `n`x`n` chessboard."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def board_deepcopy(board):
    """Deep copy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board

def get_solution(board):
    """Get queen positions from the board."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution

def xout(board, row, col):
    """Mark non-attacking positions as 'x'."""
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for dr, dc in dirs:
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board):
            if board[r][c] != 'Q':
                board[r][c] = 'x'
            r, c = r + dr, c + dc

def recursive_solve(board, row, queens, solutions):
    """Solve N-queens puzzle recursively."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("Usage: nqueens N (N >= 4)")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

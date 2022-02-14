import sys
from sudoku_utils import SudokuBoard

class SudokuSolver:
    def __init__(self, sudoku_board):
        self.board_list = self.get_board_list(sudoku_board) 
        self.sudoku_board = SudokuBoard(self.board_list)

    def solve(self):
        return self.sudoku_board.solve_board()

    def get_board_list(self, board):
        board_list = []
        for row in board:
            for elem in row:
                board_list.append(elem)
        return board_list

def solve_board(sudoku_board):
    solver = SudokuSolver(sudoku_board)
    solver.solve()
    
if __name__ == '__main__':
    board1 = [
    [0, 2, 0, 0, 9, 0, 1, 0, 0],
    [0, 0, 7, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 6, 0],
    [0, 0, 1, 9, 0, 4, 0, 0, 0],
    [0, 0, 0, 6, 0, 5, 0, 0, 7],
    [8, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 8, 5],
    [4, 9, 0, 0, 3, 0, 0, 0, 0]
    ]
    board2 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    board3 = [
    [5, 3, 8, 0, 1, 0, 0, 0, 0],
    [0, 7, 9, 6, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 2, 0, 0, 0],
    [0, 0, 7, 0, 2, 3, 4, 0, 0],
    [0, 0, 5, 0, 8, 0, 0, 0, 9],
    [4, 6, 0, 0, 9, 0, 0, 0, 1],
    [0, 9, 0, 2, 3, 4, 1, 5, 0],
    [0, 4, 1, 5, 0, 0, 2, 0, 0],
    [0, 0, 0, 8, 6, 1, 0, 3, 0]
    ]

    board4 = [
    [0, 2, 0, 0, 9, 0, 1, 0, 0],
    [0, 0, 7, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 6, 0],
    [0, 0, 1, 9, 0, 4, 0, 0, 0],
    [0, 0, 0, 6, 0, 5, 0, 0, 7],
    [8, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 8, 5],
    [4, 9, 0, 0, 3, 0, 0, 0, 0]
    ]

    solve_board(board1)
    solve_board(board2)
    solve_board(board3)
    solve_board(board4)
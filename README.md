# sudoku-solver

Python based sudoku solver for 9x9 sudoku. The algorithm picks a number for each cell that doesn't violate the row, column and subgrid constraints imposed by Sudoku
and backtrack upon encountering an invalid sudoku board state. This approach significantly reduces the search space as compared to a brute force algorithm that 
checks all 9^81 sudoku board configurations.

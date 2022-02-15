class SudokuBoard:
    def __init__(self, board_list):
        self.board = self.populate_board(board_list)
    
    def populate_board(self, board_list):
        board =  [[None for j in range(1,10)] for i in range(1,10)]
        row = 0
        for i in range(len(board_list)):
            col = i % 9

            if board_list[i] == 0:
                empty_cell_domain = {i for i in range(1,10)}
                board[row][col] = Cell(-1, empty_cell_domain)
            else:
                filled_cell_domain = set()
                board[row][col] = Cell(board_list[i], filled_cell_domain)
            
            if (i + 1) % 9 == 0:
                row += 1

        return board

    def solve_board(self):
        start_row, start_col = self.get_first_empty_cell()
        num_backtracks = Counter()
        self.bt_solver(start_row, start_col, num_backtracks)
        print('Number of Backtracks:', num_backtracks.count)
        self.display_board()
        return self.board

    def bt_solver(self, row, col, num_backtracks):
        if row == None and col == None:
            return True
        next_row, next_col = self.get_next_empty_cell(row, col)
        for value in self.board[row][col].domain:
            if self.is_valid(value, row, col):
                self.board[row][col].val = value
                if self.bt_solver(next_row, next_col, num_backtracks) == True:
                    return True
        self.board[row][col].val = -1
        num_backtracks.count += 1
        return False

    def get_next_empty_cell(self, row, col):
        for j in range(col + 1, len(self.board[0])):
            cell = self.board[row][j]
            if cell.val == -1:
                return row, j
        
        for i in range(row + 1, len(self.board)):
            for j in range(len(self.board[0])):
                cell = self.board[i][j]
                if cell.val == -1:
                    return i, j
        
        return None, None
    
    def is_valid(self, value, row, col):
        return self.valid_row(value, row, col) and self.valid_column(value, row, col) and self.valid_subgrid(value, row, col)

    def valid_row(self, value, row, col):
        for j in range(len(self.board[0])):
            cell = self.board[row][j]
            if cell.val == value:
                return False     
        return True

    def valid_column(self, value, row, col):
        for i in range(len(self.board)):
            cell = self.board[i][col]
            if cell.val == value:
                return False
        return True

    def valid_subgrid(self, value, row, col):
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        end_row = start_row + 2
        end_col = start_col + 2
        while start_row < end_row and start_col < end_col:
            for i in range(start_row, end_row):
                cell = self.board[i][start_col]
                if cell.val == value:
                    return False
            
            for j in range(start_col, end_col):
                cell = self.board[end_row][j]
                if cell.val == value:
                    return False
            
            for i in range(end_row, start_row, -1):
                cell = self.board[i][end_col]
                if cell.val == value:
                    return False
            
            for j in range(end_col, start_col, -1):
                cell = self.board[start_row][j]
                if cell.val == value:
                    return False
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1
        
        return start_row, start_col, self.board[start_row][start_col].val != value

    def get_first_empty_cell(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                cell = self.board[row][col]
                if cell.val == - 1:
                    return row, col
        return None, None

    def display_board(self):
        board_string = []
        for row in self.board:
            for cell in row:
                if len(str(cell.val)) == 1:
                    board_string.append(' ' + str(cell.val))
                else:
                    board_string.append(str(cell.val))
                board_string.append(' ')
            board_string.append('\n')
        board_string = ''.join(board_string)
        print(board_string)


class Cell:
    def __init__(self, val, domain):
        self.val = val
        self.domain = domain

    def __repr__(self):
        return str(self.val)

class Counter:
    def __init__(self, count=0):
        self.count = count
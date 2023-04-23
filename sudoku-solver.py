board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

def solveSudoku(board):
    def findEmptyCell():
        for row in range(len(board[0])):
            for col in range(len(board)):
                if board[row][col] == '.':
                    return row, col
        return None

    
    def isValid(row, col, value):
        # row
        if value in board[row]:
            return False
        # column
        if value in [board[i][col] for i in range(9)]:
            return False
        # 3X3 box
        sub_row = row//3
        sub_col = col//3
        for i in range(sub_row*3, (sub_row*3)+3):
            for j in range(sub_col*3, (sub_col*3)+3):
                if board[i][j] == value and (i,j) != value:
                    return False
        return True
    
    def solve():
        empty_cell = findEmptyCell()
        if empty_cell is None:
            return True
        row, col = empty_cell
        for value in range(1, 10):
            if isValid(row, col, str(value)):
                board[row][col] = str(value)
                if solve():
                    return True
                board[row][col] = '.'
        return False
    
    solve()
    return board
solved_board = solveSudoku(board)
for row in solved_board:
    print(row)

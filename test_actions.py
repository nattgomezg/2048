
def test_move():
    board = create_new_board()
    board[0][0] = 2
    move("down", board)
    end_board = create_new_board()
    end_board[3][0] = 2
    assert board == end_board

def test_merge(board):
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == row [i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0

    new_row = [tile for tile in row if tile!= 0]
    new_row += [0] * (len(row) - len(new_row))
    row[:] = new_row

return board

import random

def add_new_tile(board):
    import random 

def place_piece(board):
    empty_positions = [(row, col) for row in range(len(board)) for col in range(len(board[0])) if board[row][col] == 0]
    if empty_positions:
        row, col = random.choice(empty_positions)
    board[row][col] = random.choices([2,4], weights=[9, 1], k=1)[0]
    return board

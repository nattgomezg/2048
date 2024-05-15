# testing actions for the game
from game.board import create_new_board
from game.board import drop_piece
#import the actions from the game board
def test_drop_piece():
    #defining the action test drop
    board = create_new_board()
    drop_piece(board, 0, 2)
    #indicating where to drop it
    assert board == [['', '', '', ''],
                     ['', '', '', ''],
                     ['', '', '', ''],
                     ['', '', '', '2']]
    
def test_move():
    #defining the action of test move
    board = create_new_board()
    board[0][0] = 2
    #indicating where to move
    move("down", board)
    end_board = create_new_board()
    #indicating that when the board ends to insert a new one
    end_board[3][0] = 2
    #defining what the board ending is
    assert board == end_board

def test_merge(board):
    #defining the test merge action
    for row in board:
        # making numbers merge with a loop
        for i in range(len(row) - 1):
            if row[i] == row [i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0

    new_row = [tile for tile in row if tile!= 0]
    new_row += [0] * (len(row) - len(new_row))
    row[:] = new_row

return board

def create_new_board():
    board = [["", "", "", ""],
             ["", "", "", ""],
             ["", "", "", ""],
             ["", "", "", ""]]
    return board

def print_board(board):
    print(
        f"""
{board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]}
-----------
{board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]}
-----------
{board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]}
-----------
{board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]}
"""
    )

def move(direction, current_board):
    pass

def check_game_over(current_board):
    pass

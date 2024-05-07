import random

def move(current_board, direction):
    for col in range(3, -1, -1):
        # print(current_board[0][col])
        current_board[0][3] = current_board[0][col]

def add_new_tile(current_board):
    
    current_board[0][0] = random.choices([2, 4, 8], [9, 4, 1], k=1)[0]

def check_game_over(current_board):
    pass

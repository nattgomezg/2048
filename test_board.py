import random 

def place_piece(board):
    empty_positions = [(row, col) for row in range(len(board)) for col in range(len(board[0])) if board[row][col] == 0]
    if empty_positions:
        row, col = random.choice(empty_positions)
    board[row][col] = random.choices([2,4], weights=[9, 1], k=1)[0]
    return board

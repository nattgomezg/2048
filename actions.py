import random
# function for directions
def move(current_board, directions):
    # conditional statements to make the numbers stay in their places 
    if directions == "right": 
        for row in range(4):  
            for col in range(3, -1, -1):
                # print(current_board[0][col])
                if current_board[row][3] != " ":
                    current_board[row][2] = current_board[row][col]
                else:
                    # eliminating numbers so they do not stay copied on the board
                    current_board[row][3] = current_board[row][col]
                current_board[row][col] = " "
    # inidicating that numbers should go down 
    elif directions == "down":
        for col in range(4):  
            for row in range(3, -1, -1):
                # eliminating numbers so they do not stay copied on the board
                current_board[3][col] = current_board[row][col]
                current_board[row][col] = " "


def add_new_tile(current_board):
    # name: link
    # empty_positions = [(row, col) for row in range(len(current_board)) for col in range(len(current_board[0])) if current_board[row][col] == 0]
    # if empty_positions:
    #     row, col = random.choice(empty_positions)
    #     current_board[row][col] = random.choices([2, 4], [9, 1], k=1)[0]

    current_board[0][0] = random.choices([2, 4, 8], [9, 4, 1], k=1)[0]

def check_game_over(current_board):
    pass

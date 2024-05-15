from board import create_new_board, print_board
from actions import  add_new_tile, move

with open('README.md', 'r') as f:
    print(f.read())

# Setup phase
board = create_new_board()

while True:
    # Input / per-turn phase
    add_new_tile(board)
    print_board(board)
    command = input("Enter a comand: ")

    if command == "right":
        # Per-command phase
        move(board, "right")
    elif command == "left":
        move(board, "left")
    elif command == "up":
        move(board, "up")
    elif command == "down":
        move(board, "down")
    elif command == "new board":
        create_new_board()
    elif command == "game over":
        if check_game_over(board):
            print_board(board)
    elif command == "game over":
        if check_game_over(board):
            print("Game Over :( )")
        else:
            print("Game is not over yet.")
    else:
        print("I did not understand.")
    #if told another thing indicate that it doesn't respond to that

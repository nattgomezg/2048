from board import create_new_board, print_board, move_up, move_down, move_left, move_right, check_game_over

with open('README.md', 'r') as f:
    print(f.read())

while True:
    command = input("Enter a command:")
    if command == "right":
        move_right()
    elif command == "left":
        move_left()
    elif command == "up":
        move_up()
    elif command == "down":
        move_down()
    elif command == "new board":
        create_new_board and print_board()
    elif command == "game over":
        check_game_over()
    else:
        print("I did not understand this command.")

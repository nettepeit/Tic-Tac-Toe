from art import welcome, tie, x_win, o_win

board = ["-" for x in range(10)]
turn = 0


def print_board(board):
    print()
    print("     Let's Play! " + "      Positions")
    print("      " + board[0] + " | " + board[1] + " | " + board[2] + "        1" + " | " + "2" + " | " + "3")
    print("     ---+---+---" + "      ---+---+---")
    print("      " + board[3] + " | " + board[4] + " | " + board[5] + "        4" + " | " + "5" + " | " + "6")
    print("     ---+---+---" + "      ---+---+---")
    print("      " + board[6] + " | " + board[7] + " | " + board[8] + "        7" + " | " + "8" + " | " + "9" "\n")


def choose_position():
    global turn
    if turn % 2:
        marker = "O"
        print(f"It is player {marker} turn.")
    else:
        marker = "X"
        print(f"It is Player {marker} turn.")

    try:
        pos = int(input("Choose position from 1-9: "))
        pos = pos - 1
        if board[pos] == "-":
            turn += 1
            board[pos] = marker
        else:
            print("Position not empty! Choose again.")
    except IndexError:
        print("Choose a valid position number!")
    except ValueError:
        print("Choose a valid position number!")


def check_win():
    if (board[0] == board[1] == board[2] != "-" or board[3] == board[4] == board[5] != "-" or
            board[6] == board[7] == board[8] != "-" or board[0] == board[3] == board[6] != "-" or
            board[1] == board[4] == board[7] != "-" or board[2] == board[5] == board[8] != "-" or
            board[0] == board[4] == board[8] != "-" or board[2] == board[4] == board[6] != "-"):
        if turn % 2:
            print(x_win)
        else:
            print(o_win)
        return True


def board_full():
    if board.count("-") > 1:
        return False
    else:
        return True


while True:
    ans = input("Press any key to start or q to quit: ")
    print(welcome)
    if ans == "q":
        print("Thank you for playing!❤️")
        break
    else:
        board = ["-" for i in range(10)]
        turn = 0

    while not board_full():
        print_board(board)
        if check_win():
            break
        else:
            choose_position()

    else:
        print_board(board)
        if check_win():
            continue
        else:
            print(tie)

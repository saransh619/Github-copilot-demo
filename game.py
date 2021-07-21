# tick tac toe game in python 
def game():
    board = [0,1,2,3,4,5,6,7,8]
    end = False
    win = False
    count = 0
    while not end:
        print_board()
        end = check_win(board)
        print("")
        if not end:
            move = input("where do you want to move? ")
            move = int(move)
            if board[move] == "X" or board[move] == "O":
                print("invalid move")
            else:
                board[move] = "X"
                count += 1
                print("")
                if count == 9:
                    print("game over")
                    print("")
                    print_board()
                    end = True
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    
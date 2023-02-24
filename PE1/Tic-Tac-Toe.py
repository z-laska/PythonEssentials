from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("", "-" * 7, "-" * 7, "-" * 7, sep="+", end="+\n")

    for row in board:
        print("", " " * 7, " " * 7, " " * 7, sep="|", end="|\n")
        print("", "   " + str(row[0]) + "   ", "   " + str(row[1]) + "   ", "   " + str(row[2]) + "   ", sep="|",
              end="|\n")
        print("", " " * 7, " " * 7, " " * 7, sep="|", end="|\n")
        print("", "-" * 7, "-" * 7, "-" * 7, sep="+", end="+\n")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("Enter your move: "))
        except:
            print("I don't know what to do with your input. Try again!")
            continue

        if (move < 0) or (move > 9):
            print("Oops, that's not a valid move. Try again!")
            continue

        r = (move - 1) // 3
        c = (move - 1) % 3

        if (r, c) not in make_list_of_free_fields(board):
            print("Oops, that's not a valid move. Try again!")
            continue

        break

    board[r][c] = "O"


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for r in range(3):
        for c in range(3):
            if board[r][c] != "O" and board[r][c] != "X":
                free_squares.append((r, c))
    return free_squares


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        move = randrange(8)
        r = (move - 1) // 3
        c = (move - 1) % 3
        if (r, c) not in make_list_of_free_fields(board):
            continue
        break

    board[r][c] = "X"


def main():
    board = [[i for i in range(j, j + 3)] for j in range(1, 8, 3)]

    while True:
        draw_move(board)
        display_board(board)
        if victory_for(board, "X"):
            print("The computer won!")
            break
        enter_move(board)
        display_board(board)
        if victory_for(board, "O"):
            print("You won!")
            break

        if not make_list_of_free_fields(board):
            print("A tie! There is no winner this time.")
            break


main()

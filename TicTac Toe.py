import copy

def draw_board(board):
    """
    Draws a 3x3 Tic Tac Toe board to the console.
    :param board: a 3x3 board
    :return: None
    """
    if len(board) != 3:
        return
    for row in board:
        if len(row) != 3:
            return

    for row in board:
        print(row)

def available_cells(board):
    cells = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == " ":
                cells.append((i, j))
    return cells

def player_choice(available_cells):
    """
    Prompt player to choose a cell.
    :param available_cells: List of tuples of indices of empty cells.
    :return: Tuple (row, col) or None if invalid input
    """
    print("\nAvailable cells are {}\n".format(available_cells))
    choice = input("Please select the cell that you want to place your mark on: ")

    if "," not in choice:
        return None

    s = choice.split(",")

    if len(s) != 2:
        return None

    first, second = s[0].strip(), s[1].strip()
    if not first.isnumeric() or not second.isnumeric():
        return None

    row, col = int(first), int(second)

    if row < 0 or row > 2 or col < 0 or col > 2:
        return "Out of range"

    return row, col

def check_row(board, row):
    return board[row][0] == board[row][1] == board[row][2] != " "

def check_col(board, col):
    return board[0][col] == board[1][col] == board[2][col] != " "

def check_diagonal(board):
    first_diagonal = board[0][0] == board[1][1] == board[2][2] != " "
    second_diagonal = board[0][2] == board[1][1] == board[2][0] != " "
    return first_diagonal or second_diagonal

def game_over(board):
    """
    Determines if the game has ended and who, if anyone, has won.
    :param board: the game's board
    :return: -1 if the game did not end, 0 if the game ended with no winner, 1 if player 1 won, 2 if player 2 won
    """
    for index in range(3):
        if check_row(board, index):
            return 1 if board[index][0] == "X" else 2

        if check_col(board, index):
            return 1 if board[0][index] == "X" else 2

    if check_diagonal(board):
        return 1 if board[1][1] == "X" else 2

    if all(" " not in row for row in board):
        return 0
    return -1

def tic_tac_toe():
    row = [" "] * 3
    board = [copy.copy(row) for _ in range(3)]
    player_turn = 0

    while game_over(board) == -1:
        draw_board(board)
        cells = available_cells(board)
        choice = player_choice(cells)
        if choice is None:
            print("The format inserted was not correct")
        elif choice == "Out of range":
            print("Integers must be between 0 and 2")
        else:
            row, col = choice
            if board[row][col] == " ":
                board[row][col] = "X" if player_turn == 0 else "O"
                player_turn = 1 - player_turn
            else:
                print("Cell is already taken. Please try again.")

    result = game_over(board)
    if result == 0:
        print("Tie")
    else:
        print("Player {} Won!".format(result))

tic_tac_toe()

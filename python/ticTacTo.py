def print_board(board):
    """Print the current state of the Tic Tac Toe board"""
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def get_player_move(board, player):
    """Ask the player for their move and validate it"""
    while True:
        move = input("Player " + player + " please make a move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == " ":
            return int(move)
        else:
            print("Invalid move, please try again.")

def check_winner(board):
    """Check if there's a winner or a tie"""
    for i in range(0, 9, 3):
        # Check rows
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return board[i]
        # Check columns
        if board[i//3] == board[i//3+3] == board[i//3+6] and board[i//3] != " ":
            return board[i//3]
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != " ":
        return board[2]
    # Check for tie
    if " " not in board:
        return "Tie"
    # No winner yet
    return None

def play_game():
    """Play a game of Tic Tac Toe"""
    board = [" "] * 9
    players = ["X", "O"]
    current_player = players[0]
    
    while True:
        print_board(board)
        move = get_player_move(board, current_player)
        board[move - 1] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Tie":
                print("It's a tie!")
            else:
                print("Player " + winner + " wins!")
            return
        # Switch players
        current_player = players[1] if current_player == players[0] else players[0]

play_game()

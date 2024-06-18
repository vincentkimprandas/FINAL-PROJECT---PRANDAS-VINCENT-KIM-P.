def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def main():
    print("Welcome to Tic-Tac-Toe!")

    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")

    current_player = player1
    turn = 0

    while True:
        print("\n" + current_player + "'s turn:")
        print_board(board)

        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if board[row][col] == " ":
                board[row][col] = "X" if current_player == player1 else "O"
                break
            else:
                print("That position is already taken. Try again.")

        if check_winner(board):
            print_board(board)
            print(f"Congratulations! {current_player} wins!")
            break

        turn += 1
        if turn == 9:
            print_board(board)
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
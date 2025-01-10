# Dibuat Oleh : Revan Kautsar Mulyana (90% AI)
# Tanggal     : 10-01-2025
# PROJECT 100
import math

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there's a winner or if the game is a draw."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    for row in board:
        if " " in row:
            return None  # Game is still ongoing

    return "Draw"  # No moves left, it's a draw

def minimax(board, depth, is_maximizing):
    """Minimax algorithm for optimal AI moves."""
    winner = check_winner(board)
    if winner == "O":
        return 10 - depth
    elif winner == "X":
        return depth - 10
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    """Find the best move for AI (O)."""
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    """Main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True  # True if it's the player's turn (X)

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        if player_turn:
            print("Your turn (X). Enter row and column (1-3):")
            try:
                row, col = map(int, input().split())
                row, col = row - 1, col - 1
                if board[row][col] == " ":
                    board[row][col] = "X"
                    player_turn = False
                else:
                    print("Cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter two numbers between 1 and 3.")
        else:
            print("AI's turn (O)...")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "O"
            player_turn = True

        print_board(board)

if __name__ == "__main__":
    main()

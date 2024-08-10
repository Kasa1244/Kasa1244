#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

# Constants for players
PLAYER_X = -1
PLAYER_O = 1

# Initialize the game board
def create_board():
    return [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

# Check for a winner
def check_victory(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Check for a draw
def is_stalemate(board):
    return all([cell != 0 for row in board for cell in row])

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if check_victory(board, PLAYER_O):
        return 1
    if check_victory(board, PLAYER_X):
        return -1
    if is_stalemate(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = 0
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = 0
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Determine the best move for the AI
def find_best_move(board):
    best_value = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = PLAYER_O
                move_value = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = 0
                if move_value > best_value:
                    best_move = (i, j)
                    best_value = move_value
    return best_move

# Print the current game board
def display_board(board):
    for row in board:
        print(' '.join(['X' if cell == PLAYER_X else 'O' if cell == PLAYER_O else '-' for cell in row]))
    print()

# Main game loop
def start_game():
    board = create_board()
    while True:
        display_board(board)
        if check_victory(board, PLAYER_O):
            print("AI wins!")
            break
        if check_victory(board, PLAYER_X):
            print("Human wins!")
            break
        if is_stalemate(board):
            print("It's a draw!")
            break

        if sum([row.count(0) for row in board]) % 2 == 0:
            # AI's turn
            move = find_best_move(board)
            board[move[0]][move[1]] = PLAYER_O
        else:
            # Human's turn
            while True:
                human_move = input("Enter your move (row and column, e.g., '1 2'): ").split()
                if len(human_move) != 2:
                    print("Invalid input. Please enter two numbers separated by a space.")
                    continue
                try:
                    row, col = int(human_move[0]), int(human_move[1])
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                    continue
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid move. Row and column must be between 0 and 2.")
                    continue
                if board[row][col] != 0:
                    print("Invalid move. The cell is already occupied.")
                    continue
                board[row][col] = PLAYER_X
                break

start_game()


# In[ ]:





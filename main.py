board = [
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         ]

open_row_at_col = [5,5,5,5,5,5,5]


def print_board():
    for r in range(len(board)):
        for c in range(len(board[0])):
            print(board[r][c], end=" ")
        print()

def check_winner():
    rows = len(board)
    cols = len(board[0])

    # Check horizontal win
    for row in range(rows):
        for col in range(cols - 3):  # Only need to check up to 4 consecutive
            if board[row][col] != 0 and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                return board[row][col]

    # Check vertical win
    for row in range(rows - 3):  # Only need to check up to 4 consecutive
        for col in range(cols):
            if board[row][col] != 0 and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return board[row][col]

    # Check diagonal (bottom-left to top-right)
    for row in range(rows - 3):  # Only need to check rows that have 4 consecutive spaces up
        for col in range(cols - 3):  # Only need to check cols that have 4 consecutive spaces right
            if board[row][col] != 0 and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return board[row][col]

    # Check diagonal (top-left to bottom-right)
    for row in range(3, rows):  # Only need to check rows that have 4 consecutive spaces down
        for col in range(cols - 3):  # Only need to check cols that have 4 consecutive spaces right
            if board[row][col] != 0 and board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                return board[row][col]

    # If no winner, return 0
    return 0
        

def game_loop():
    player_turn = True
    while True:
        print_board()
        winner = check_winner()
        if winner != 0:
            print(f"winner is {winner}")
            break
        if player_turn:
            while True:
                col = int(input("Player 1: "))
                if(col<1 or col>7):
                    print(f"column {col} out of bounds (1-7) try again")
                elif(open_row_at_col[col-1]==-1):
                    print(f"column {col} is full pick another in bounds")
                else:
                    break
            col -=1  
            row = open_row_at_col[col]    
            board[row][col] = 1
            open_row_at_col[col] -=1
            player_turn = False
            print(open_row_at_col)
        else:
            while True:
                col = int(input("player 2: "))
                
                if(col<1 or col>7):
                    print(f"column {col} out of bounds (1-7) try again")
                elif(open_row_at_col[col-1]==-1):
                    print(f"column {col} is full pick another in bounds")
                else:
                    break
            col -=1  
            row = open_row_at_col[col]    
            board[row][col] = 2
            open_row_at_col[col] -=1
            player_turn = True
            print(open_row_at_col)









if __name__ == "__main__":
    game_loop()
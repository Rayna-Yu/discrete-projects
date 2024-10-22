import random

# asks the user what player they want to be
while True:
    player_str = input("Which player? (1/2)")
    if player_str in ['1', '2']:
        player = int(player_str)
        break
    else:
        print("not an option, please enter 1 or 2")
print(f"playing as player {player}.")

# set up random board 
def makeboard():
    board = []
    randomrows = random.randint(1,8)
    for x in range(randomrows):
        board.append(random.randint(1, 7))
    return board

board = makeboard() # makes the initial board


# game logic
def playgame(board):
    max_row = max(board)
    max_row_index = board.index(max_row)
    # checks if it is given a winningboard
    # if it does plays a random move
    if winningboard(board):
        index = random.randint(0, len(board) - 1)
        board[index] = random.randint(0, board[index])
        return board
    # if not finds the largest row and subtracts one from it until the board becomes winning
    else:
        for i in range(max_row):
            board[max_row_index] -= 1
            if winningboard(board):
                return board
            else: 
                continue
        return board
            

# adds the rows with xor to get the nim sum
def addnimbits(board):
    nim_sum = 0
    for row in board:
        nim_sum ^= row
    return nim_sum
    
# tells if its a winning board by seeing it the nim sum is 0
def winningboard(board):
    return addnimbits(board) == 0

# checks to see if the game has ended
def game_end(board):
    return sum(board) == 0

def nextplayer(currentplayer):
    if currentplayer == 1:
        return 2
    else: return 1

def drawboard(board):
    for row in range(len(board)):
        print("X" * board[row])

currentplayer = 1 # sets initial player to 1

# plays the game
while not game_end(board):
    drawboard(board)
    if currentplayer == player:
        print("your turn!")
        while True:
            try:
                player_move_row = int(input("Which row would you like to play? (Enter a number): "))
                if 1 <= player_move_row <= len(board):  # Checking valid row
                    player_move_blocks = int(input("How many blocks do you want to take? "))
                    if 0 < player_move_blocks <= board[player_move_row - 1]:  # Checking valid block amount
                        board[player_move_row - 1] -= player_move_blocks
                        currentplayer = nextplayer(currentplayer)  # Switch to computer
                        break
                    else:
                        print("Not a valid block amount. Please pick another block!")
                else:
                    print("Not a valid row. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        print("computers turn!")
        playgame(board)  # computer plays
        currentplayer = nextplayer(currentplayer) # switch to user
print("Final board state:", board)








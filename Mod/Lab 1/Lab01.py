# 1. Name:
#      Ben Painter
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of the assignment for me was probably the saving and loading functions of the game.
#      The concept was pretty simple and I knew how i was going to do it, but I kept running into bugs that
#      I made. But once I figured out the few different spots that I was doing wrong, like not actually saving
#      the current board, but instead just the same blank board everytime, I got it to work just fine. I've also
#      never had to make a saving feature in a program before, so it was pretty fun. 
# 5. How long did it take for you to complete the assignment?
#      4 hours

import json
from json import encoder

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.

blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    
    # If the file does exist, then it will return the data of that file.
    try:
        with open(filename) as file:   
            data = json.load(file)
            return data

    # If filename does not exist, return a blank_board.
    except:
        return blank_board
        
def save_board(filename, board):
    '''Save the current game to a file.'''
    with open(filename, 'w') as outfile:
        json.dump(board, outfile)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Returns True if it is X's turn
    num_of_BLANK = 0
    for i in board:
        if i == BLANK:
            num_of_BLANK = num_of_BLANK + 1
    if (num_of_BLANK % 2) == 0:
        return False
    else:
        return True

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    if is_x_turn(board):
        user_move = input("X> ")
    else:
        user_move = input("O> ")

    if user_move == "q":
        return False
    elif int(user_move) > 9 or int(user_move) < 1:
        return board
    elif board[int(user_move) - 1] == BLANK:
        if is_x_turn(board):
            board[int(user_move) - 1] = X
        else:
            board[int(user_move) - 1] = O

    return board

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

keep_playing = True
current_board = read_board("saved_data.txt")

while(game_done(current_board["board"], True) != True and keep_playing):
    display_board(current_board["board"])
    updated_board = play_game(current_board["board"])
    if (updated_board == False):
        save_board("saved_data.txt", current_board)
        keep_playing = False
    else:
        current_board["board"] = updated_board

if keep_playing:
    save_board("saved_data.txt", blank_board)
    display_board(current_board["board"])
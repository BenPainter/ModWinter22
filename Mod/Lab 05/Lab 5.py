# 1. Name:
#      Ben Painter
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This file will allow the player to make changes to the board. No rules are being checked yet
# 4. What was the hardest part? Be as specific as possible.
#      The harderst part was probably making sure all of the rows were lined up with their labels.
#      For some reason, that took the longest amount of time to get right. 
# 5. How long did it take for you to complete the assignment?
#      3 hours

import json


def main():
    board, filename = choose_file()
    keep_playing = True
    while keep_playing:
        display(board)
        player_input = user_input(board, filename)
        if player_input != "Q":
            board = update_board(player_input, board)
        else:
            keep_playing = False





def update_board(player_input, board):
    #Takes the user's input and processes it down into readable values for the board and updates it
    column = int(player_input[0])
    row = int(player_input[1])
    board_row = board[row]

    #storing the new value into board
    board_row[column] = int(player_input[2])   
    board[row] = board_row
    return board

def display(board):
    #displays the current board
    row_header = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("   A B C   D E F   G H I", end=" ")
    for i in range(len(board)):
        print("")
        if i == 3 or i == 6:
            print("  ---------------------")
        counter = 0
        print(row_header[i], end="  ")
        for j in board[i]:
            counter = counter + 1
            if counter == 4 or counter == 7:
                print("|",end = " ")
            if j > 0:
                print(j, end=" ")
            else:
                print(" ", end=" ")

def choose_file():
    #This function takes the user's input and feeds it to read_file for processing
    level = int(input("Please choose the level you would like to work on?(1-3): "))
    board, filename = read_file(level)
    return board, filename

def read_file(level):
    #This file reads the json files and returns the board and filename
    if level == 1:
        with open('Easy.json') as file:   
            data = json.load(file)
            filename = 'Easy.json'
            board = data["board"]
            return board, filename
    elif level == 2:
        with open("Medium.json") as file:   
            data = json.load(file)
            filename = 'Medium.json'
            board = data["board"]
            return board, filename
    elif level == 3:
        with open("Hard.json") as file:   
            data = json.load(file)
            filename = 'Hard.json'
            board = data["board"]
            return board, filename
    else:
        print("ERROR")
        

def user_input(board, filename):
    #This gets the user's input and then either returns it all, or saves the file to quit
    valid_input = False
    while valid_input == False:
        print("\nSpecify a coordinate to edit or 'Q' to save and quit")
        player_input = input("")
        if player_input != "Q" and len(player_input) == 2:
            position = input(f"What number goes into {player_input}? ")
            
            #Breaking down the letter into a number
            column = ord(player_input[0].lower()) - 97
            row = int(player_input[1]) - 1
            simplified_input = str(column) + str(row) + str(position)
            if ruler_checker(simplified_input, board):
                valid_input = True
                
            
        elif player_input == "Q" or player_input == "q":
            save_file(board, filename)
            valid_input = True
            simplified_input = "Q"
        else:
            print("Please put in a valid input")
    
    return simplified_input

def save_file(board, filename):

    data = {'board':board}
    #Saves the current board to the file
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

#These functions will be used in the final draft
def possible_num():
    pass

def ruler_checker(player_input, board):
    if is_filled(player_input, board):
        return True
    else:
        return False

def hor_check():
    pass

def ver_check():
    pass

def block_check():
    pass

def is_filled(player_input, board):
    
    return True


main()
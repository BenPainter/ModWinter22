# 1. Name:
#      Ben Painter
# 2. Assignment Name:
#      Lab 06 : Sudoku Draft
# 3. Assignment Description:
#      The program allows the user to play Sudoku by typing in
#      a valid placement and then the number they wish to place.
#      All the basic rules are enforced.
# 4. What was the hardest part? Be as specific as possible.
#       The harderst part was getting allowing the player to see the 
#       The possible numbers in a given spot. I kept running into a problem
#       because one of my rule checker wasn't working correctly. 
# 5. How long did it take for you to complete the assignment?
#       6 hours

import json
import math


def main():
    board, filename = choose_file()
    keep_playing = True
    while keep_playing:
        display(board)
        player_input = user_input(board, filename)
        if player_input != "Q" and player_input != "P":
            board = update_board(player_input, board)
        elif player_input == "Q":
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
    level_valid = False
    while not level_valid:
        level_num = input("Please choose the level you would like to work on?(1-3): ")
        try: 
            level = int(level_num[0])
            if level > 0 and level < 4: 
                level_valid = True
        except:
            print("Please put in a whole number from 1 to 3")

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

        if len(player_input) == 2 or len(player_input) == 1:
            

            if len(player_input) == 2:
                
                correct_order = False
                try:
                    column = ord(player_input[0].lower()) - 97
                    row = int(player_input[1]) - 1
                    correct_order = True
                except:
                    try:
                        column = ord(player_input[1].lower()) - 97
                        row = int(player_input[0]) - 1
                        correct_order = True
                    except:
                        print("You need to put a letter and a number")

                if correct_order and (row > 0 and row < 9) and (column > 0 and column < 9):
                    user_num = input(f"What number goes into {player_input}? ")           
                    
                    if int(user_num) > 0 and int(user_num) < 10:
                        
                        simplified_input = str(column) + str(row) + str(user_num)
                        #Simplified_input = "Column+Row+Value"
                        if is_filled(simplified_input, board) and ruler_checker(simplified_input, board):
                            valid_input = True
                     
                
            elif player_input == "Q" or player_input == "q":
                save_file(board, filename)
                valid_input = True
                simplified_input = "Q"
            
            elif player_input == "P" or player_input == "p":
                check_place = input("Where would you like to see the possible numbers? ")
                correct_order = False
                try:
                    column = ord(check_place[0].lower()) - 97
                    row = int(check_place[1]) - 1
                    correct_order = True
                except:
                    try:
                        column = ord(check_place[1].lower()) - 97
                        row = int(check_place[0]) - 1
                        correct_order = True
                    except:
                        print("You need to put a letter and a number")
                
                if correct_order and (row > 0 and row < 9) and (column > 0 and column < 9):
                    check_input = str(column) + str(row)
                    if is_filled(check_input, board):
                        valid_input = True
                        possible_num(check_input, board)
                    simplified_input = "P"
            
            
            else:
                print("Please put in a valid input")

        else:
            print("Sorry, but I don't understand where that postion is. Be sure to check you're")
            print("in the range of A-I and 1-9")
        
    return simplified_input

def save_file(board, filename):

    data = {'board':board}
    #Saves the current board to the file
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


def possible_num(player_input, board):
    valid_nums = []
    for test_num in range (1, 10):
        player_input = player_input + str(test_num)
        if ruler_checker(player_input, board):
            valid_nums.append(test_num)
        player_input = player_input[:-1]
    for num in valid_nums:
        print(num, end=" ")

    print("")


def ruler_checker(player_input, board):
    if not ver_check(player_input, board):
        return False
    elif not hor_check(player_input, board):
        return False
    elif not block_check(player_input, board):
        return False
    else:
        return True
    

def hor_check(player_input, board):
    no_matched = True
    for i in board[int(player_input[1])]:
        if i == int(player_input[2]):
            #print("Can't have the same number in the same row")
            no_matched = False
    
    return no_matched

def ver_check(player_input, board):
    no_matched = True
    for i in range (0, len(board)):        
        if board[i][int(player_input[0])] == int(player_input[2]):
            #print("Can't have the same number in the same column")
            no_matched = False
    
    return no_matched

def block_check(player_input, board):
    no_matched = True
    block_column = math.ceil((int(player_input[0])+1) / 3)
    block_row = math.ceil((int(player_input[1])+1) / 3)

    for i_row in range((block_row * 3) - 3, (block_row * 3)):
        for i_column in range((block_column * 3) - 3, (block_column * 3)):
            if board[i_row][i_column] == int(player_input[2]):
                no_matched = False
    
    return no_matched

def is_filled(player_input, board):
    if board[int(player_input[1])][int(player_input[0])] == 0:
        return True
    else:
        print("There is already a number here")
        return False

main()
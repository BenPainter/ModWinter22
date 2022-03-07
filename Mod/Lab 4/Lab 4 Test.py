
board = [
    [ 7, 2, 3, 0, 0, 0, 1, 5, 9 ],
    [ 6, 0, 0, 3, 0, 2, 0, 0, 8 ],
    [ 8, 0, 0, 0, 1, 0, 0, 0, 2 ],
    [ 0, 7, 0, 6, 5, 4, 0, 2, 0 ],
    [ 0, 0, 4, 2, 0, 7, 3, 0, 0 ],
    [ 0, 5, 0, 9, 3, 1, 0, 4, 0 ],
    [ 5, 0, 0, 0, 7, 0, 0, 0, 3 ],
    [ 4, 0, 0, 1, 0, 3, 0, 0, 6 ],
    [ 9, 3, 2, 0, 0, 0, 7, 1, 4 ]
  ]





def display(board):
    print(board)

    for i in range(len(board)):
        print("")
        if i == 3 or i == 6:
            print("---------------------")
        counter = 0
        for j in board[i]:
            counter = counter + 1
            if counter == 4 or counter == 7:
                print("|",end = " ")
            if j > 0:
                print(j, end=" ")
            else:
                print(" ", end=" ")

'''

function display(board):

    For row in range(length(board)):
        If row = 3 OR row = 6:
            Put("----------------------")
        
        counter <- 0
        For value in board[row]:
            counter <- counter + 1
            If counter = 4 OR counter = 7:
                Put("|", end = " ")
            If value > 0:
                Put(value, end = " ")
            Else:
                Put(" ", end = " ")







'''





display(board)

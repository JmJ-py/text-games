def main():

#Step 1 is print the rules and have the user return nothing
    print("This is tic tac toe. You will go first and be the X.\n"
      "The board will appear as follows.\n\n"
      " 1|2|3 \n"
      " -----\n"
      " 4|5|6 \n"
      " -----\n"
      " 7|8|9 \n\n"
      "From left to right, top to bottom, the positions are represented"
      "by 1 through 9\n\n")
    input("Press Enter to continue.")
   
    win = "no win"
    while win != "win":
        place_x()
        print_board()
        if check_win() is True:
            win = "win"
            break
        if check_tie(board) is True:
            print("\n\nIt's a tie!!!\nPlay Again!")
            break
        place_o()
        print_board()
        if check_win() is True:
            win = "win"
            break
        if check_tie(board) is True:
            print("\n\nIt's a tie!!!\nPlay Again!")
            break

        
    
board = {
    0: " ", 1: "|", 2: " ", 3: "|", 4: " ", 5: "\n", 
    6: "-", 7: "-", 8: "-", 9: "-", 10: "-", 11: "\n" ,
    12: " ", 13: "|", 14: " ", 15: "|", 16: " ", 17: "\n",
    18: "-", 19: "-", 20: "-", 21: "-", 22: "-", 23: "\n",
    24: " ", 25: "|", 26: " ", 27: "|", 28: " "
}

open_positions = {
    1: 0, 2: 2, 3: 4, 4: 12, 5: 14, 6: 16, 7: 24, 8: 26, 9: 28
}

#Step 2 is take the user input on position and determine the location in the print
def place_x():
    open_positions = {1: 0, 2: 2, 3: 4, 4: 12, 5: 14, 6: 16, 7: 24, 8: 26, 9: 28}
    position = int(input("\nWhat position do you want to place your X?: "))   
    position = open_positions[position]
    if board.get(position) != " ":
        print("Ooops. That position is already taken.")
        place_x()
    else:
        board[position] = "X"

def place_o():
    open_positions = {1: 0, 2: 2, 3: 4, 4: 12, 5: 14, 6: 16, 7: 24, 8: 26, 9: 28}
    position = int(input("\nWhat position do you want to place your O?: "))
    position = open_positions[position]
    if board.get(position) != " ":
        print("Ooops. That position is already taken.")
        place_o()
    else:
        board[position] = "O"

    
        
def check_win():
    #checks rows
    for i in range(0, 25, 12):
        if board[i] == board[i + 2] == board[i + 4] == "X":
            print("\nWinner Winner Chicken Dinner\nThe Xs have won!")
            return True
    for i in range(0, 25, 12):
        if board[i] == board[i + 2] == board[i + 4] == "O":
            print("\nWinner Winner Chicken Dinner\nThe Os have won!")
            return True
    
    #checks columns
    for i in range(0, 5, 2):
        if board[i] == board[i + 12] == board[i + 24] == "X":
            print("\nWinner Winner Chicken Dinner\nThe Xs have won!")
            return True
        if board[i] == board[i + 12] == board[i + 24] == "O":
            print("\nWinner Winner Chicken Dinner\nThe Os have won!")
            return True
        
    #checks diagonals
    if board[0] == board[14] == board[28] == "X":
        print("\nWinner Winner Chicken Dinner\nThe Xs have won!")
        return True
    if board[0] == board[14] == board[28] == "O":
        print("\nWinner Winner Chicken Dinner\nThe Os have won!")
        return True
    if board[4] == board[14] == board[24] == "X":
        print("\nWinner Winner Chicken Dinner\nThe Xs have won!")
        return True
    if board[4] == board[14] == board[24] == "O":
        print("\nWinner Winner Chicken Dinner\nThe Os have won!")
        return True
  

def check_tie(a):
    value = " "
    if value in a.values():
        return
    else:
        return True


def print_board():
    for value in board.values():
        print(value, end="")


main()

import sys

def main():

    board = {
        0: " ", 1: "|", 2: " ", 3: "|", 4: " ", 5: "\n", 
        6: "-", 7: "-", 8: "-", 9: "-", 10: "-", 11: "\n" ,
        12: " ", 13: "|", 14: " ", 15: "|", 16: " ", 17: "\n",
        18: "-", 19: "-", 20: "-", 21: "-", 22: "-", 23: "\n",
        24: " ", 25: "|", 26: " ", 27: "|", 28: " "
        }


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
        place_x(board)
        print_board(board)
        if check_win(board) is True:
            if play_again() is True:
                reset_board(board)
            else:
                win = "win"
                break
        if check_tie(board) is True:
            print("\nIt's a tie!")
            if play_again() is True:
                reset_board(board)
        place_o(board)
        print_board(board)
        if check_win(board) is True:
            if play_again() is True:
                reset_board(board)
            else:
                win = "win"
                break

        
   
#Step 2 is take the user input on position and determine the location in the print
def place_x(j):
    open_positions = {1: 0, 2: 2, 3: 4, 4: 12, 5: 14, 6: 16, 7: 24, 8: 26, 9: 28}
    
    position = int(input("\n\nWhat position do you want to place your X?: "))    
    position = open_positions[position]
    if j.get(position) != " ":
        print("Ooops. That position is already taken.")
        place_x(j)
    else:
        j[position] = "X"

def place_o(k):
    open_positions = {1: 0, 2: 2, 3: 4, 4: 12, 5: 14, 6: 16, 7: 24, 8: 26, 9: 28}

    position = int(input("\n\nWhat position do you want to place your O?: "))   
    position = open_positions[position]
    if k.get(position) != " ":
        print("Ooops. That position is already taken.")
        place_o(k)
    else:
        k[position] = "O"

    
        
def check_win(m):
    #checks rows
    for i in range(0, 25, 12):
        if m[i] == m[i + 2] == m[i + 4] == "X":
            print("\nWinner Winner Chicken Dinner\nThe Xs have won!")
            return True
    for i in range(0, 25, 12):
        if m[i] == m[i + 2] == m[i + 4] == "O":
            print("\nWinner Winner Chicken Dinner\nThe Os have won!")
            return True
    
    #checks columns
    for i in range(0, 5, 2):
        if m[i] == m[i + 12] == m[i + 24] == "X":
            print("\nWinner Winner Chicken Dinner\nThe Xs have won!")
            return True
        if m[i] == m[i + 12] == m[i + 24] == "O":
            print("\nWinner Winner Chicken Dinner\nThe Os have won!")
            return True
        
    #checks diagonals
    if m[0] == m[14] == m[28] == "X":
        print("\nWinner Winner Chicken Dinner\nThe Xs have won!")
        return True
    if m[0] == m[14] == m[28] == "O":
        print("\nWinner Winner Chicken Dinner\nThe Os have won!")
        return True
    if m[4] == m[14] == m[24] == "X":
        print("\nWinner Winner Chicken Dinner\nThe Xs have won!")
        return True
    if m[4] == m[14] == m[24] == "O":
        print("\nWinner Winner Chicken Dinner\nThe Os have won!")
        return True
  

def check_tie(a):
    empty = " "
    if empty in a.values():
        return
    else:
        return True


def print_board(l):
    for char in l.values():
        print(char, end="")

def play_again():
    yes = ["y", "Y", "Yes", "yes"]
    if input("\nPlay again? (Y/N): ").strip() in yes:
        main()
    else:
        sys.exit()

def clear_board():

    return {
    0: " ", 1: "|", 2: " ", 3: "|", 4: " ", 5: "\n", 
    6: "-", 7: "-", 8: "-", 9: "-", 10: "-", 11: "\n" ,
    12: " ", 13: "|", 14: " ", 15: "|", 16: " ", 17: "\n",
    18: "-", 19: "-", 20: "-", 21: "-", 22: "-", 23: "\n",
    24: " ", 25: "|", 26: " ", 27: "|", 28: " "
    }

def reset_board(b):
    b = clear_board()
    return b



if __name__ == "__main__":
    main()

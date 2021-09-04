# blank board

def blank_board():
    row1 = [1,2,3]
    row2 = [4,5,6]
    row3 = [7,8,9]
    return row1, row2, row3

def play_again():
    while True:
        user_input = input('Would you like to play again? (Y/n) ')
        if user_input == 'Y':
            return True
        elif user_input == 'n':
            return False
        else:
            continue




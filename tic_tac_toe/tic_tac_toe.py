while True:
    print("Welcome to this text-based game of Tic Tac Toe\n" +
          "In this game you play using your keyboard. Ready to start? (Y/n)")
    user_input = input('Type your answer: ')
    if user_input == 'Y':
        break
    else:
        continue

print("Here we go...")

# Display new board
from game_utils import new_game as n, board_functions as b

row1, row2, row3 = n.blank_board()
b.display_board(row1, row2, row3)



player = 1

while True:

    if player%2 == 1:
        counter = 'X'
    elif player%2 == 0:
        counter = 'O'


    # ask player where to place their counter
    print(f'Player {counter} goes next')

    while True:
    # keeps asking player for input until legal move given
        row_selection, col_selection = b.ask_player()
        if b.check_move([row1,row2,row3], row_selection, col_selection) is True:
            print('Legal move')
            break
        else:
            print('Illegal Move')
            continue

    print('updating grid...')
    row_list = [row1,row2,row3]
    row_list[row_selection][col_selection] = counter


    if b.check_win(row1,row2,row3):
        b.display_board(row1, row2, row3)
        print(f'Player {counter} wins!!')

        if n.play_again():
            row1, row2, row3 = n.blank_board()
        else:
            break

    elif b.check_full([row1,row2,row3]):
        b.display_board(row1, row2, row3)
        print("It's a draw!")

        if n.play_again():
            row1, row2, row3 = n.blank_board()
        else:
            break

    player += 1
    print('This is what the board looks like:')
    b.display_board(row1, row2, row3)




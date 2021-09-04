def display_board(row1,row2,row3):
    '''
    Given the game-state passed into this function row by row,
    this function will display this in a user-friendly format
    '''

    for i in [row1, row2, row3]:
        print('----------')
        print(i[0],'|',i[1],'|',i[2])
    print('----------')


def ask_player():
    print('Which row would you like to place your counter?')
    while True:
        row = input('Top (t), Middle (m) or Bottom (b)? ')
        if row in ['t','m','b']:
            break
        else:
            continue
    print('Which column would you like to place your counter?')
    while True:
        col = input('Left (l), Middle (m) or Right (r)? ')
        if col in ['l','m','r']:
            break
        else:
            continue

    # Return a number for row and column
    if row == 't':
        row_selection = 0
    if row == 'm':
        row_selection = 1
    if row == 'b':
        row_selection = 2

    if col == 'l':
        col_selection = 0
    if col == 'm':
        col_selection = 1
    if col == 'r':
        col_selection = 2

    return row_selection, col_selection

def check_move(rows, row_selection, col_selection):

    if type(rows[row_selection][col_selection]) == int:
        return True
    else:
        return False

def check_win(row1,row2,row3):
    # Checking horizontals
    for i in [row1,row2,row3]:
        if i[0]==i[1]==i[2]:
            return True

    # checking verticals
    for i in [0,1,2]:
        if row1[i] == row2[i] == row3[i]:
            return True

    # Check diagonals
    if row1[0] == row2[1] == row3[2]:
        return True
    if row1[-1] == row2[-2] == row3[-3]:
        return True

    # All other cases:
    return False

def check_full(rows):
    '''
    This function will check the board to see if it's full.
    Returns False if there are spaces to fill.
    '''
    for i in rows:
        for j in [0,1,2]:
            if type(i[j]) == int:
                return False
    return True

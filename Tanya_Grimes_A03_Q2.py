# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
Tic Tac Toe

Created on Sat Jun 20 17:35:51 2020

@author: Tanya Grimes
'''


#-----------------------------------------------------
# Variable and Constant Definitions


P1_ICON = 'X'
P2_ICON = 'O'
EMPTY_ICON = '_'

gameplay = []
userplay = dict()
positions_played = []
c = 0

# populates 3 x 3 matrix with empty icon
for col in range(3):
    gameplay.append([])
    for row in range(3):
        # preps the grid with a placeholder icon to visualize the game
        gameplay[col].append(EMPTY_ICON)
        c += 1
        
        # userplay will keep track of each number played as
        # a key and the value is the corresponding gameplay position
        userplay[c] = (col, row)
 

#-----------------------------------------------------
# Function Definitions

def display_grid():
    # displays current gameplay in a grid
    for row in range(3):
        for col in range(3):
            print('\t',gameplay[row][col], end='\t')
        print('\n')


def find_positions(player):
    # checks for horizontal win
    for h in range(3):
        if len(set(gameplay[h])) == 1 and gameplay[h][0] == player:
            
            display_grid()
            print('\nPlayer '+str(player), 'won horizontally')
            return True
    
    
    # checks for vertical win
    for v in range(3):
        if (len(set((gameplay[0][v],gameplay[1][v],gameplay[2][v]))) == 1 and 
            gameplay[0][v] == player):
            
            display_grid()
            print('\nPlayer '+str(player), 'won vertically')
            return True
    
              
    # checks for diagonal win, left to right (from the top)
    if (len(set([gameplay[d][d] for d in range(3)])) == 1 and
        gameplay[1][1] == player):
        
        display_grid()
        print('\nPlayer '+str(player), 'won diagonally')
        return True
    
    
    # checks for diagonal win, right to left (from the top)
    if (len(set([gameplay[d][abs(2-d)] for d in range(3)])) == 1 and
        gameplay[1][1] == player):
        
        display_grid()
        print('\nPlayer '+str(player), 'won diagonally')
        return True
    
   
def check_for_win():
    # calls to check game state, based on positions played
    
    p1won = find_positions(P1_ICON)
    p2won = False if p1won else find_positions(P2_ICON)
    
    if not p1won and not p2won and len(positions_played) == 9:
        display_grid()
        
        # currently no check to see how many winning moves are left for
        # each player, so draw count flags when all 9 positions are filled
        print('\nAww! It\'s a Draw!')
        
    elif p1won:
        print('Congratulations Player', P1_ICON + '!')
        
    elif p2won:
        print('Congratulations Player', P2_ICON + '!')
        
    else:
        # continues game play
        return 'y'
        
    return 'n'


def validate_player_input(u_input):
    # validates various input and prints a message
    # conditions split for ease in validating, even if
    # message is the same
    
    if len(u_input) == 0 or not u_input.isnumeric():
        # checks for empty or non-numeric input
        print('Please enter an integer between 1 and 9.\n')
        display_grid()
        
    elif type(u_input) == float:
        # checks for floats
        print('Please enter an integer between 1 and 9.\n')
        display_grid()
        
    elif int(u_input) < 1 or int(u_input) > 9:
        # checks for integers outside of specified range
        print('Please enter an integer between 1 and 9.\n')
        display_grid()
        
    else:
        return True
    
    return False


def retrieve_player_input(player):
    # recursively validates the input and only returns when valid
    
    p_input = input('Player ' + player + ' select position: ').strip()
        
    if validate_player_input(p_input) == True:
        return p_input
    else:
        return retrieve_player_input(player)

      
def start_game():
    run = 'y'
    p1_play_count = 0
    
    # keep getting user input until one of the ends occurs
    while (run != 'n'):
        display_grid()
        
        # add user input for player 2 and validate
        p1_input = retrieve_player_input(P1_ICON)
        print()
        
        p1_int = int(p1_input)
        x = userplay[p1_int][0]
        y = userplay[p1_int][1]
        
        # add p1_input to gameplay location
        if gameplay[x][y] == EMPTY_ICON:
            
            # keep track of plays to determine when to start checking 
            # for wins
            p1_play_count += 1
            
            # assign player 1 value to the grid
            gameplay[x][y] = P1_ICON
            positions_played.append(p1_int)
            
            # only need to start checking for a win when player 1 has 
            # 3 moves or more
            if p1_play_count > 2:
                run = check_for_win()
                if run == 'n': continue
            
            display_grid()
            
            # add user input for player 2 and validate
            p2_input = retrieve_player_input(P2_ICON)
            print()
            
            # shorten position reference for gameplay
            p2_int = int(p2_input)
            a = userplay[p2_int][0]
            b = userplay[p2_int][1]
            
            while gameplay[a][b] != EMPTY_ICON:
                print('Position already taken\n\n')
                
                display_grid()
                
                # add user input for player 2 and validate
                p2_input = retrieve_player_input(P2_ICON)
                print()
                
                p2_int = int(p2_input)
                a = userplay[p2_int][0]
                b = userplay[p2_int][1]
                
            else:
                # assign player 2 value to the grid
                gameplay[a][b] = P2_ICON
                positions_played.append(p2_int)
                
                # only need to start checking for a win when player 1 has 
                # 3 moves or more
                if p1_play_count > 2:
                    run = check_for_win()
            
        else:
            print('\nPosition already taken')
            continue
        

#-----------------------------------------------------
# Instructions and Game Start


print('\n---------------------------------------------')
print('* Tic-Tac-Toe: 2 Player')
print('* Player', P1_ICON, 'starts first.')
print('* Players alternate entering values 1 to 9 to')
print('  get three of them in a row using the grid:')
print('  1    2    3')
print('  4    5    6')
print('  7    8    9')
print('* If there is no win, game results in a draw')
print('  after filling in all the positions since')
print('  there is currently no tracker for possible ')
print('  remaining player moves')
print('---------------------------------------------\n')

start_game()











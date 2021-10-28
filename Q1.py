import random
from colorama import Fore
import datetime

game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

def menu():
    print("Welcom to \"Tic Tac Toe\"")
    print("Select one of the following options:")
    print("1. Single player(with computer)")
    print("2. Double player")

    choice = int(input("--> "))
    return choice


def show_game_board():
    for i in range(3):
        for j in range(3):
            if game[i][j] == 'X':
                print(Fore.RED + 'X', end = ' ')
            elif game[i][j] == 'O':
                print(Fore.BLUE + 'O', end = ' ')
            else:
                print(Fore.RESET + game[i][j], end = ' ')
        print(Fore.RESET)


def get_from_player(name, sign):
    while True:
        print(name)
        row = int(input('row: '))
        col = int(input('col: '))

        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '-':
                game[row][col] = sign
                break
            else:
                print('This cell is NOT empty! Please try again.')
        else:
            print('row and col must be between 0 and 2!')
            

def get_from_computer():
    print("Computer")

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        
        if game[row][col] == '-':
            game[row][col] = 'O'
            print('row:', row)
            print('col:', col)
            break


def check_win(sign):
    win = False

    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == sign:
            win = True
            return win
        
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] == sign:
            win = True
            return win
    
    if game[0][0] == game[1][1] == game[2][2] == sign:
        win = True
        return win
    
    if game[0][2] == game[1][1] == game[2][0] == sign:
        win = True
        return win

    return win


def check_draw():
    if not any('-' in i for i in game):
        return True
    else:
        return False
               

def check_game(name, sign):
    if check_win(sign) == True:
        print(name + " wins!")
        end_time = datetime.datetime.now().replace(microsecond =0 )
        print("Game Duration:", end_time - start_time)
        exit()
    else:
        if check_draw() == True:
            print("Draw!")
            end_time = datetime.datetime.now().replace(microsecond = 0)
            print("Game Duration:", end_time - start_time)
            exit()
        else:
            return
    

result = menu()
if result == 1:
    start_time = datetime.datetime.now().replace(microsecond = 0)
    show_game_board()

    while True:
        get_from_player("Player", 'X')
        show_game_board()
        check_game("Player 1", 'X')
        
            
        get_from_computer()
        show_game_board()
        check_game("Computer", 'O')

elif result == 2:
    start_time = datetime.datetime.now().replace(microsecond = 0)
    show_game_board()

    while True:
        get_from_player("Player 1", 'X')
        show_game_board()
        check_game("Player 1", 'X')

        get_from_player("Player 2", 'O')
        show_game_board()
        check_game("Player 2", 'O')


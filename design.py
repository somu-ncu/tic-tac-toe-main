# Game design

def gameStart():
    # Game start design

    print("\n=====TIC TAC TOE GAME=====\n\n")
    print("# RULES\n")
    print("1. User will be required to enter the row and column number of the position where he/she wants to place the turn.")
    print("\n2. User will be represented by X and system will be represented by O.\n\nEnjoy the game!!!\n")

def gameBoard():
    # Game Board

    gameBoard = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    return gameBoard

def printBoard(b):
    # Print board

    print ('  ', ' 1  ', ' 2  ', ' 3  ')
    print('1', b[0])
    print('2', b[1])
    print('3', b[2])

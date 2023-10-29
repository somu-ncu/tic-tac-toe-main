# TIC-TAC-TOE 
# Classic tic tac toe game made using python with AI support.
#
# Author : github.com/Raveesh1505

from errorHandle import *
from design import *
import random


def validation(uRow, uColumn):
    """
    This function validates the move of the user.
    If the user enters any value out of range 1 to 3
    the function will invalidate the move and tell the
    user to enter valid input again.
    """

    validInput = [1, 2, 3]
    if uRow and uColumn in validInput:
        return True
    else:
        return False


def gameCheck(b):
    """
    This function determines the winner if the
    game. By sensing various possible winning patterns,
    the game will determine who the winner will be and
    whether to end the game or not.
    """


    if ["X", "X", "X"] in b:
        return 1
    elif ["O", "O", "O"] in b:
        return 2
    elif  ["X", "X", "X"] == [b[0][0], b[1][0], b[2][0]]:
        return 1
    elif  ["X", "X", "X"] == [b[0][1], b[1][1], b[2][1]]:
        return 1
    elif  ["X", "X", "X"] == [b[0][2], b[1][2], b[2][2]]:
        return 1
    elif  ["X", "X", "X"] == [b[0][0], b[1][1], b[2][2]]:
        return 1
    elif  ["X", "X", "X"] == [b[0][2], b[1][1], b[2][0]]:
        return 1
    elif  ["O", "O", "O"] == [b[0][0], b[1][0], b[2][0]]:
        return 2
    elif  ["O", "O", "O"] == [b[0][1], b[1][1], b[2][1]]:
        return 2
    elif  ["O", "O", "O"] == [b[0][2], b[1][2], b[2][2]]:
        return 2
    elif  ["O", "O", "O"] == [b[0][0], b[1][1], b[2][2]]:
        return 2
    elif  ["O", "O", "O"] == [b[0][2], b[1][1], b[2][0]]:
        return 2
    else:
        return 3


def game():
    '''
    Main game script
    '''

    gameStart()

    b = gameBoard()
    printBoard(b)


    while (gameCheck(b) == 3):    # Continue to run the game till it is over
        Combinations = []

        # User attempt
        userRow = int(input("Row : "))
        userColumn = int(input("Column : "))

        if validation(userRow, userColumn):
            if [userRow, userColumn] in Combinations:
                print(spaceOccupied())
            else:
                b[userRow-1][userColumn-1] = "X"
                Combinations.append([userRow, userColumn])
        else:
            print(invalidInput())

        # System attempt
        sysRow = random.randint(1, 3)
        sysColumn = random.randint(1, 3)
        if [sysRow, sysColumn] in Combinations:
            print(spaceOccupied())
        else:
            b[sysRow-1][sysColumn-1] = "O"
            Combinations.append([sysRow, sysColumn])
        
        printBoard(b)

    if gameCheck(b) == 1:
        print("User won")
    elif gameCheck(b) == 2:
        print("System won")


if __name__ == "__main__":
    game()
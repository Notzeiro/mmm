from random import randrange
 
for i in range(10):
    print(randrange(8))

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move=input("Enter your move:\n")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    board[row][column]
    board=[left=[upperL=False , centerL=False , bottomL=False] ,
            center=[upperC=False , centerC=False , bottomC=False] ,
             right=[upperR=False , centerR=False , bottomR=False]]

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.
        print(f"+-------+-------+-------+\
                |       |       |       |\
                |   {}  |   {}  |   {}  |\
                |       |       |       |\
                +-------+-------+-------+\
                |       |       |       |\
                |   {}  |   {}  |   {}  |\
                |       |       |       |\
                +-------+-------+-------+\
                |       |       |       |\
                |   {}  |   {}  |   {}  |\
                |       |       |       |\
                +-------+-------+-------+")

draw_move()
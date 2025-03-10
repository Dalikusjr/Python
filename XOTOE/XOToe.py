from random import randrange
board=[["1","2","3"],["4","X","6"],["7","8","9"]]
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    # La fonction accepte un paramètre contenant l'état
    # actuel du tableau et l'affiche dans la console.
    for i in range(len(board)):
        j=0
        print("+------+------+------+")
        print("|      |      |      |")
        print("|  ",board[i][j]," |"," ",board[i][j+1]," |"," ",board[i][j+2]," |")
        print("|      |      |      |")   
    print("+------+------+------+")        
            
def enter_move(board):
    while victory_for(board, sign)== None:
        while True:
            move=int(input("Enter your move: "))
            if move<10 and move>0:
                break
            else:print("Wrong command..")
        move=str(move)
        x=False
        for i in range(3):
            if x== False:
                for j in range(3):
                    if move == board[i][j]:
                        board[i][j]="O"
                        x=True
                        break
                    else:
                        x=False
            else:break
        if x==False:
            print("Wrong command..")
        else:
            break
    display_board(board)
def draw_move(board):
    # The function draws the computer's move and updates the board.
    # La fonction génère le coup de l'ordinateur et met à jour le plateau de jeu.
    print("My Turn")
    while  victory_for(board, sign)== None:
        y=randrange(9)
        y=str(y)
        x=False
        for j in range(len(board)):
            if x==False:
                for k in range(len(board[j])):
                    if y == board[j][k]:
                        board[j][k]="X"
                        x=True
                        break
            else:
                break
        if x==True:
            break
    display_board(board)
def make_list_of_free_fields(board):
    free=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["O","X"]:
                free.append((i,j))
    return free
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # La fonction examine la situation sur le plateau pour déterminer si le participant
    # utilisant les 'O' ou les 'X' a remporté la partie.
        j=0
        test=False
        for i in range(3):
            if board[i][j]+board[i][j+1]+board[i][j+2]in ["OOO","XXX"]:
                test=True
                break
            elif board[j][i]+board[j+1][i]+board[j+2][i]in ["OOO","XXX"]:
                test=True
                break
        if board[0][0]+board[1][1]+board[2][2]in ["OOO","XXX"]:
            test=True
        elif board[0][2]+board[1][1]+board[2][0]in ["OOO","XXX"]:
            test=True
        if test==False and sign==0:
            who="T"
            return who
        elif test==True and sign % 2 != 0:
            who="U"
            return who
        elif test==True and sign % 2 == 0:
            who="M"
            return who
        else: return None
sign=8
who=""
print("Here we goooo...")
display_board(board)
while victory_for(board, sign)== None:
    if sign % 2 == 0:
        enter_move(board)
    else:
        draw_move(board)
    sign=len(make_list_of_free_fields(board))
who=victory_for(board, sign)
if who=="T":
    print("\nIts a Tae...")
elif who=="U":
    print("\nYou won!!")
else:
    print("\nLoooseeer")
display_board(board)
print("\nGAME OVER")



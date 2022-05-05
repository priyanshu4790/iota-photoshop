from IPython.display import clear_output 
player1=''
player2=''
player=0
board=['$',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display(num,a):
    clear_output() 
    #board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    if board[num]==' ':
        if a==1:
            board[num]='X'
        else:
            board[num]='O'
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
def reset_board():
    global board
    board=[' ']*10
def display_board():
    print('ENTER YOUR CHOICE OF BLOCK USING THE CORRESPONDING NUMBER IN THE BOX')
    print('7'+'|'+'8'+'|'+'9')
    print('-----')
    print('4'+'|'+'5'+'|'+'6')
    print('-----')
    print('1'+'|'+'2'+'|'+'3')
    print('                 ')
def check():
    if board[7]==board[9] and board[8]==board[9] and board[9]=='X':
        return 'X'
    if board[7]==board[9] and board[8]==board[9] and board[9]=='O':
        return 'O'
    if board[4]==board[5] and board[5]==board[6] and board[6]=='X':
        return 'X'
    if board[4]==board[5] and board[5]==board[6] and board[6]=='O':
        return 'O'
    if board[1]==board[2] and board[2]==board[3] and board[3]=='X':
        return 'X'
    if board[1]==board[2] and board[2]==board[3] and board[3]=='O':
        return 'O'
    if board[7]==board[4] and board[4]==board[1] and board[1]=='X':
        return 'X'
    if board[7]==board[4] and board[4]==board[1] and board[1]=='O':
        return 'O'
    if board[8]==board[5] and board[5]==board[2] and board[2]=='X':
        return 'X'
    if board[8]==board[5] and board[5]==board[2] and board[2]=='O':
        return 'O'
    if board[9]==board[6] and board[6]==board[3] and board[3]=='X':
        return 'X'
    if board[9]==board[6] and board[6]==board[3] and board[3]=='O':
        return 'O'
    if board[9]==board[5] and board[5]==board[1] and board[1]=='X':
        return 'X'
    if board[9]==board[5] and board[5]==board[1] and board[1]=='O':
        return 'O'
    if board[7]==board[5] and board[5]==board[3] and board[3]=='X':
        return 'X'
    if board[7]==board[5] and board[5]==board[3] and board[3]=='O':
        return 'O'
    if board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' ':
        return 'tie'
def inpu():
        clear_output()
        marker=''
        P1=input('Enter player 1 name: ')
        P2=input('Enter player 2 name: ')
        while(marker!='X' and  marker!='x' and marker!='O' and  marker!= 'o'):
            marker=input(f'{P1} choose X or O: ')
            
        player1 = marker.upper()
        if player1 == 'X' or player1 == 'x':
            print(f'{P1} is X')
            print(f'{P2} is O')
            player2='O'
        else:
            player2='X'
            print(f'{P1} is O')
            print(f'{P2} is X')
        chance=[1,2]*100
        for l in chance:
            if l==1 :
                if player1=='X' or player1=='x':
                    players=1
                else:
                    players=2
                display_board()
                s=int(input(f'{P1} choose position to mark: '))
                display(s,players)
            else:
                if player2=='X' or player2=='x':
                    players=1
                else:
                    players=2
                display_board()
                s=int(input(f'{P2} choose position to mark: '))
                display(s,players)
            if check()==player1:
                print(f'CONGRATULATIONS {P1} HAS WON')
                f=input('Do you want to play again? Yes or no: ')
                f=f.upper()
                if f=='YES':
                    reset_board()
                    #global board
                    #board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                    inpu()
                break
            elif check()==player2:
                print(f'CONGRATULATIONS {P2} HAS WON')
                f=input('Do you want to play again? Yes or no: ')
                f=f.upper()
                if f=='YES':
                    reset_board()
                    #global board
                    #board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                    inpu()
                break
            elif check()=='tie':
                print('MATCH TIED')
                f=input('Do you want to play again? Yes or no: ')
                f=f.upper()
                if f=='YES':
                    reset_board()
                   # global board
                    #board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                    inpu()
                break
                
inpu()
import sys
def is_X_winner(matrix_):
    for i in range(3):
        if matrix_[i] == ["X", "X", "X"] or [row[i] for row in matrix_] == ["X", "X", "X"]:
            return True
    if [matrix_[i][i] for i in range(3)] == ["X", "X", "X"]:
        return True
    if [matrix_[2 - i][i] for i in range(3)] == ["X", "X", "X"]:
        return True
    return False
def is_O_winner(matrix_):
    for i in range(3):
        if matrix_[i] == ["O", "O", "O"] or [row[i] for row in matrix_] == ["O", "O", "O"]:
            return True
    if [matrix_[i][i] for i in range(3)] == ["O", "O", "O"]:
        return True
    if [matrix_[2 - i][i] for i in range(3)] == ["O", "O", "O"]:
        return True
    return False
def check(indexx,indexy,player):
    if(indexx not in [0,1,2] or indexy not in [0,1,2]):
        print("Coordinates should be from 1 to 3!")
        return 0
    elif(mat[indexx][indexy]!='_'):
        print("This cell is occupied! Choose another one!")
        return 0
    else:
        mat[indexx][indexy]='X' if player%2==1 else 'O'
        return 1
def printmat():
    print("---------")
    print("| ",end='')
    [[print(mat[j][i] if mat[j][i]!='_' else " ",end=' ') if i!=2  else print(mat[j][i] if mat[j][i]!='_' else " ","|\n|",end=' ') for i in range(len(mat[j]))] if j!=2 else [print(mat[j][i] if mat[j][i]!='_' else " ",end=' ') if i!=2  else print(mat[j][i] if mat[j][i]!='_' else " ","|") for i in range(len(mat[j]))] for j in range(len(mat))]
    print("---------")
def inpt():
    global player
    try:
        indexx,indexy=list(map(int,input("Enter the coordinates:").split()))
    except:
        print("You should enter numbers!")
        return
    indexx, indexy = indexy, indexx;
    indexx = 3 - indexx;
    indexy -= 1
    if not check(indexx, indexy,player):
        inpt()
    else:
        printmat()
        player+=1
mat=[['_','_','_'],['_','_','_'],['_','_','_']]
printmat()
player=1
while(True):
    inpt()
    if is_X_winner(mat):
        print("X wins")
        sys.exit()
    if is_O_winner(mat):
        print("O wins")
        sys.exit()
    li=[1 if '_' not in i else 0 for i in mat ]
    if all(li):
        print("Draw")
        player=1
        mat=[['_','_','_'],['_','_','_'],['_','_','_']]
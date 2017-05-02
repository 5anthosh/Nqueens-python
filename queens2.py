def initialise(board,n):
    for key in ['queen','row','col','NWtoSE','SWtoNE']:
        board[key]={}
    for i in range(n):
        board['queen'][i]=-1
        board['row'][i]=0
        board['col'][i]=0
    for i in range(-(n-1),n):
        board['NWtoSE'][i]=0
    for i in range(2*n-1):
        board['SWtoNE'][i]=0
a=[]
def printboard(board):
    b=[]
    for row in sorted(board['queen'].keys()):
        b.append((row,board['queen'][row]))
    a.append(b)
    del b
    b=[]
def free(i,j,board):
    return(board['row'][i]==0 and board['col'][j]==0 and board['NWtoSE'][j-i]==0 and board['SWtoNE'][j+i]==0)
def addqueen(i,j,board):
    board['queen'][i]=j
    board['row'][i] =1
    board['col'][j] = 1
    board['NWtoSE'][j-i] = 1
    board['SWtoNE'][j+i] = 1


def undoqueen(i, j, board):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['NWtoSE'][j-i] = 0
    board['SWtoNE'][j+i] = 0
count = 0


def placequeen(i, board):
    n=len(board['queen'].keys())
    for j in range(n):
        if free(i, j, board):
            addqueen(i, j, board)
            if i == n-1:
                printboard(board)
            else:
                placequeen(i+1, board)
            undoqueen(i, j, board)
checkpoint = 0
print("start the program (yes/no)")
while True:
    try:
        option = input('input: ')
    except:
        print("string only".center(60,'-'))
    else:
        if option != 'Yes' and option != 'yes' and option != 'No' and option != 'no':
            print("enter appropriate option".center(60, '-'))
            continue
        if option == 'yes' or option == 'Yes':
            while True:
                try:
                    board = {}
                    n = int(input("enter the number of queens: "))
                    if n <= 3:
                        print("number greater than 3 only".center(60, '-'))
                        continue
                except:
                    print("integer only".center(60, '-'))
                    continue
                else:
                    initialise(board, n)
                    if placequeen(0, board):
                        printboard(board)
                    dec = n*4
                    print('number of possible boards: ', len(a))
                    while True:
                        try:
                            numboards = int(input('how many boards do you want to print: '))
                            print('\n')
                        except:
                            print("only integers".center(60, '-'))
                            continue
                        else:
                            if numboards == 0:
                                print(None)
                                print('\n', "exited".center(60, '-'), '\n', sep='')
                                exit()
                            elif numboards > len(a):
                                print(' ', (str(numboards)+' greater than possible boards').center(75, '-'), sep='')
                                print("try again.........")
                                continue
                            for i in a[0:numboards]:
                                matrix = [[' ' for i in range(n)]for j in range(n)]
                                for j in i:
                                    u, v = j
                                    matrix[u][v] = 'Q'
                                print('\n', ('board  '+str(a.index(i)+1)).center(60, '-'), '\n', sep='')
                                for k in matrix:
                                    print('\n', '+---'*n, sep='', end='')
                                    print('+')
                                    for x in k:
                                        print('|', x, end=' ')
                                    print('|', end=' ')
                                    if matrix.index(k) == len(k)-1:
                                        print('\n', '+---'*n, sep='', end='')
                                        print('+')
                                del matrix
                            del a
                            quit1 = 0
                            break
                break
        if option == 'no' or option == 'No' or quit1 == 0:
            print('\n', "exited".center(60, '-'), '\n', sep='')
            break

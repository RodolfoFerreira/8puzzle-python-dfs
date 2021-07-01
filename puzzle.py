from copy import deepcopy
import numpy as np

initState=np.array([
            [1,2,3],
            [8,0,4],
            [7,6,5]
        ])

goalState=np.array([
            [2,8,1],
            [0,4,3],
            [7,6,5]
        ])

fringe = []
visited = []
expandedStates = []

def moveUp(currentState):
    upState=deepcopy(currentState)
    position=np.where(currentState == 0)

    if (position[0] == 0):
        return None
    else:
        i=position[0]
        j=position[1]
        temp=upState[i, j]
        upState[i, j]=upState[i - 1, j]
        upState[i - 1, j]=temp

    if ((upState == currentState).all()):
        return None
    elif (arreq_in_list(upState, expandedStates)):
        return None 
    else:
        expandedStates.append(deepcopy(upState))
        return upState
        
def moveDown(currentState):
    downState=deepcopy(currentState)
    position=np.where(currentState == 0)

    if (position[0] == 2):
        return None
    else:
        i=position[0]
        j=position[1]
        temp=downState[i, j]
        downState[i, j]=downState[i + 1, j]
        downState[i + 1, j]=temp

    if ((downState == currentState).all()):
        return None
    elif (arreq_in_list(downState, expandedStates)):
        return None
    else:
        expandedStates.append(deepcopy(downState))
        return downState

def moveRight(currentState):
    rightState=deepcopy(currentState)
    position=np.where(currentState == 0)

    if (position[1] == 2):
        return None
    else:
        i=position[0]
        j=position[1]
        temp=rightState[i, j]
        rightState[i, j]=rightState[i, j + 1]
        rightState[i, j + 1]=temp

    if ((rightState == currentState).all()):
        return None
    elif (arreq_in_list(rightState, expandedStates)):
        return None   
    else:
        expandedStates.append(deepcopy(rightState))
        return rightState

def moveLeft(currentState):
    leftState=deepcopy(currentState)
    position=np.where(currentState == 0)

    if (position[1] == 0):
        return None
    else:
        i=position[0]
        j=position[1]
        temp=leftState[i, j]
        leftState[i, j]=leftState[i, j - 1]
        leftState[i, j - 1]=temp

    if ((leftState == currentState).all()):
        return None
    elif (arreq_in_list(leftState, expandedStates)):
        return None  
    else:
        expandedStates.append(deepcopy(leftState))
        return leftState

def expandPuzzle(puzzleState):
    up = moveUp(puzzleState)
    if (up is not None):
        fringe.append(up)

    down = moveDown(puzzleState)
    if (down is not None):
        fringe.append(down)

    left = moveLeft(puzzleState)
    if (left is not None):
        fringe.append(left)

    right = moveRight(puzzleState)
    if (right is not None):
        fringe.append(right)

def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)

def getInvCount(arr) :
    inv_count = 0
    for i in range(0, 2) :
        for j in range(i + 1, 3) :
           
            # Value 0 is used for empty space
            if (arr[j][i] > 0 and arr[j][i] > arr[i][j]) :
                inv_count += 1
    return inv_count
     

def isSolvable(puzzle) :
    invCount = getInvCount(puzzle)
   
    return (invCount % 2 == 0)

def verifReachable(initialArr, finalArr):
    inv = 0
    initial = list(initialArr.flatten())
    final = list(finalArr.flatten())
    for posInit in range(0, 9): #vetor inicial
        if (initial[posInit] != 0):
            posFinal = final.index(initial[posInit])
            aux=[] #cria uma lista com todos os elementos que podem ocorrer antes do atual
            for x in range(0, posFinal):
                if (final[x] != 0):
                    aux.append(final[x])
            #print str(initial[posInit]) 
            #print aux
            for i in range(posInit, 9):
                for j in range(0, len(aux)):
                    if (initial[i] == aux[j]):
                        #print "inversao"
                        inv = inv + 1
    #print inv		
    if (inv % 2) == 0:	
        return True
    else:
        return False

def printMatrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = ["|" + fmt.format(*row) + "|" for row in s]
    print("\n".join(table))
    
i = 0
fringe.append(initState)
expandedStates.append(initState)

if(verifReachable(initState, goalState)):
    print("-"*5 + "A combinação é solucionável" + "-"*5)
    printMatrix(initState)
    print("-"*5 + "PARA" + "-"*5)
    printMatrix(goalState)

    while(len(fringe) > 0):
        print("-"*5 + "ITERAÇÃO: %d" %i)
        print("-"*5 + "FRINGE: %d" %len(fringe))
        print("-"*5 + "EXPANDED: %d" %len(expandedStates))
        print("-"*5 + "MOVIMENTOS: %d" %len(visited))
        print("-"*20)

        state = deepcopy(fringe[0])
        visited.append(state)

        if (np.array_equal(state, goalState)):
            print("Estado desejado encontrado em %d tentativa(s)" % i)
            break
        else:
            expandPuzzle(state)
            fringe.pop(0)

        i=i+1
else:
    print("A combinação não é solucionável")
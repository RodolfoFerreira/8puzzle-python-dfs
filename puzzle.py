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

i = 0
fringe.append(initState)
expandedStates.append(initState)

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
import PySimpleGUI as sg
import numpy as np

# o is 1; x is 2

isXTurn = True
game = np.zeros((3,3))


translate = {0 : " ", 1 : "O", 2 : "X"}


def isDraw():
    return False;


#returns true if someone has won
def printTurn():
    global isXTurn
    if(not hasWon()):
        if(isXTurn):
            print("it's X's Turn")
        else:
            print("it's O's Turn")
    else:
        return True


def xGoes(x,y):
    global isXTurn
    if (not isXTurn) or (not isEmpty(x,y)):
        return False
    game[x,y] = 2
    isXTurn = False
    return True


def oGoes(x,y):
    global isXTurn
    if isXTurn or (not isEmpty(x,y)):
        return False
    game[x,y] = 1
    isXTurn = True
    return True


def isEmpty(x,y):
    return game[x,y] == 0


def hasWon():
    length = range(0,3)
    for x in length:
        #check horizontal and vertical
        if allEqual(game[x,:]) and not game[x,1] == 0:
            printWon(game[x,1])
            return True
        if allEqual(game[:,x]) and not game[1,x] == 0:
            printWon(game[1,x])
            return True
        #checks diagonals
    if ((game[0,0] == game[1,1] and game[0,0] == game[2,2]) or (game[0,2] == game[1,1] and game [2,0] == game[1,1])) and not game[1,1] == 0:
        printWon(game[2,2])
        return True
    return False
    
        
#converts number to player letter and prints it with text
def printWon(player):
    x = ""
    if(player == 1):
        x = "O"
    if(player == 2):
        x = "X"
    print(x + " Wins!")


def allEqual(list):
    first = list[0]
    for elem in list:
        if elem != first:
            return False
            break
    return True


def printGame(g):
    board = " {} | {} | {} \n------------ \n {} | {} | {} \n------------ \n {} | {} | {}"
    arr = g.ravel()
    translated = [translate[x] for x in arr]
    print(board.format(*translated))


sg.theme('DarkAmber')
layout = [  [sg.Button('   '), sg.Button('   '), sg.Button('   ')],
            [sg.Button('   '), sg.Button('   '), sg.Button('   ')],
            [sg.Button('   '), sg.Button('   '), sg.Button('   ')] ]
window = sg.Window('Tic Tac Toe', layout)

while not printTurn(): 
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    # print(event)
    if(event == "   "): 
        xVal = 0
        yVal = 0
    else:
        eventNum = int(event[3:4])
        getXVal = eventNum % 3
        if(getXVal == 2):
            xVal = 0
        if(getXVal == 0):
            xVal = 1
        if(getXVal == 1):
            xVal = 2
        if(eventNum < 2):
            yVal = 0
        elif(eventNum < 5):
            yVal = 1
        elif(eventNum < 8):
            yVal = 2
    if(isXTurn):      
            xGoes(yVal,xVal)
    else:
            oGoes(yVal,xVal)
    printGame(game)

#0 is X 1 is O

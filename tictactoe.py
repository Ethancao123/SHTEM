import PySimpleGUI as sg
import numpy as np

isXTurn = True  #variable that determines whose turn it is                             
game = np.zeros((3,3)) #creates a blank 3x3 array that represents the tic tac toe game; o is 1; x is 2
translate = {0 : " ", 1 : "O", 2 : "X"} #creates a dictionary object that stores the translation between numbers and letters

#determines if the game is a draw
def isDraw(): 
    for x in range(3):
        for y in range(3):
            if(game[x,y] == 0): 
                return False #returns false if an empty location is found
    print("It's a draw")
    return True #returns true if no empty locations were found

#determines whose turn it is and returns true of a winner is found
def printTurn():
    #global isXTurn #same as the global variable isXTurn
    if(not hasWon()):
        if(isXTurn): #choses which message to print
            print("It's X's Turn")
        else:
            print("It's O's Turn")
    else:
        return True #returns this if a winner is found

#method that is called when X makes a move
def xGoes(x,y):
    global isXTurn #same as the global variable isXTurn
    if (not isXTurn) or (not isEmpty(x,y)): #checks if it is X's turn and whether the location requested is empty
        return False #returns false if the move is not valid
    game[x,y] = 2 #sets the position in the location array to represent a spot taken by X
    isXTurn = False #gives the turn to the other player
    return True #returns true to represent a valid move

#method that is called when O makes a move
def oGoes(x,y):
    global isXTurn #same as the global variable isXTurn
    if isXTurn or (not isEmpty(x,y)): #checks if it is O's turn and whether the location requested is empty
        return False #returns false if the move is not valid
    game[x,y] = 1 #sets the position in the location array to represent a spot taken by O
    isXTurn = True #gives the turn to the other player
    return True #returns true to represent a valid move

#checks a certain location is empty
def isEmpty(x,y):
    return game[x,y] == 0

#checks if a player has won the game
def hasWon():
    length = range(3) #variable to represent the dimensions of the game board
    for x in length: #checks if the spaces in any of the horizontial or vertial axis form 3 in a row and checks that they are not all empty
        if allEqual(game[x,:]) and not game[x,1] == 0:
            printWon(game[x,1])
            return True
        if allEqual(game[:,x]) and not game[1,x] == 0:
            printWon(game[1,x])
            return True
    if ((game[0,0] == game[1,1] and game[0,0] == game[2,2]) or (game[0,2] == game[1,1] and game [2,0] == game[1,1])) and not game[1,1] == 0:
        printWon(game[2,2]) #prints who won the game
        return True #returns true to represent a win
    return False #returns false to represent no winner
     
#converts number to player letter and prints it with text
def printWon(player):
    print(translate[player] + " Wins!") #uses the translate dictionary to translate the number value to a string value

#checks if a list of items is equal
def allEqual(list):
    first = list[0]
    for elem in list:
        if elem != first:
            return False #returns false if an element does not equal the first element
    return True #returns true if no different element is found

#formats the game and prints it into the terminal
def printGame(g):
    board = " {} | {} | {} \n------------ \n {} | {} | {} \n------------ \n {} | {} | {}"
    arr = g.ravel() #converts the 2d array into a 1d array
    translated = [translate[x] for x in arr] #translates all of the number values
    print(board.format(*translated)) #prints the result

#creates the gamepad with pysimplegui
sg.theme('DarkAmber')
layout = [  [sg.Button('   '), sg.Button('   '), sg.Button('   ')],
            [sg.Button('   '), sg.Button('   '), sg.Button('   ')],
            [sg.Button('   '), sg.Button('   '), sg.Button('   ')] ]
window = sg.Window('Tic Tac Toe', layout)

#loops until a player wins or the game becomes a draw
while not isDraw() and not printTurn(): 
    event, values = window.read() #reads the players input on the gamepad
    if event == sg.WIN_CLOSED: #ends if user closes window
        break
    if(event == "   "): #result if the user clicks the first button
        xVal, yVal = 0
    else:   #the output of event is presented in the form of (buttonValue + index). The first button has no index, the second is 0, the third is 1, etc.
        eventNum = int(event[3:4])  #In this case, we do not care about the button value so we remove it
        getXVal = eventNum % 3 #by taking the mod of the index, we can determine which column it is on.
        if(getXVal == 2):
            xVal = 0
        if(getXVal == 0):
            xVal = 1
        if(getXVal == 1):
            xVal = 2
        if(eventNum < 2): #the row of a button can be determined by checking if its value if between 2 numbers
            yVal = 0
        elif(eventNum < 5): #elif is used here to avoid having to test if eventNum is >= 2, as this was determined previously
            yVal = 1
        elif(eventNum < 8):
            yVal = 2
    if(isXTurn):      
            xGoes(yVal,xVal)
    else:
            oGoes(yVal,xVal)
    printGame(game)
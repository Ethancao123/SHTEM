import PySimpleGUI as sg
import numpy as np

class TTTGame:

    def __init__(self, p1, p2):
        self.playerX = p1
        self.playerO = p2
        self.xWins = 0
        self.oWins = 0
        self.draws = 0
        self.isXTurn = True
        self.game = np.zeros((3,3))
        self.translate = {0 : " ", 1 : "O", 2 : "X"}
        sg.theme('DarkAmber')
        self.layout = [  [sg.Button('   '), sg.Button('   '), sg.Button('   ')],
                [sg.Button('   '), sg.Button('   '), sg.Button('   ')],
                [sg.Button('   '), sg.Button('   '), sg.Button('   ')] ]
        self.window = sg.Window('Tic Tac Toe', layout)

    def isDraw():
        for x in range(3):
            for y in range(3):
                if(game[x,y] == 0): 
                    return False
        print("It's a draw")
        return True

    def printTurn():
        if(not hasWon()):
            if(isXTurn):
                print("It's X's Turn")
            else:
                print("It's O's Turn")
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
        length = range(3)
        for x in length:
            if allEqual(game[x,:]) and not game[x,1] == 0:
                printWon(game[x,1])
                return True
            if allEqual(game[:,x]) and not game[1,x] == 0:
                printWon(game[1,x])
                return True
        if ((game[0,0] == game[1,1] and game[0,0] == game[2,2]) or (game[0,2] == game[1,1] and game [2,0] == game[1,1])) and not game[1,1] == 0:
            printWon(game[2,2])
            return True
        return False

    def printWon(player):
        print(translate[player] + " Wins!")

    def allEqual(list):
        first = list[0]
        for elem in list:
            if elem != first:
                return False
        return True

    def printGame(g):
        board = " {} | {} | {} \n------------ \n {} | {} | {} \n------------ \n {} | {} | {}"
        arr = g.ravel()
        translated = [translate[x] for x in arr]
        print(board.format(*translated))

    def playGame():
        while not isDraw() and not printTurn():
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
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
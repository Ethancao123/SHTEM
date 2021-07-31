import PySimpleGUI as sg
import numpy as np

isXTurn = True

class TTTGame:
    def __init__(self, p1, p2):
        self.playerX = p1
        self.playerO = p2
        self.winner = "draw"
        global isXTurn
        self.game = np.zeros((3,3))
        self.translate = {0 : " ", 1 : "O", 2 : "X"}

    def isDraw(self):
        for x in range(3):
            for y in range(3):
                if(self.game[x,y] == 0):
                    return False
        #print("It's a draw")
        self.winner = "draw"
        return True

    def printTurn(self):
        if(not hasWon()):
            if(isXTurn):
                pass
                #print("It's X's Turn")
            else:
                pass
                #print("It's O's Turn")
        else:
            return True

    def makeMove(self):
        global isXTurn
        #print(isXTurn)
        if(isXTurn):
            move = self.playerX.getMove(self.game)
            if move == -1: 
                return -1
            if not self.xGoes(move[0], move[1]):
                return False
        else:
            move = self.playerO.getMove(self.game)
            if move == -1: 
                return -1
            if not self.oGoes(move[0], move[1]):
                return False
        isXTurn = not isXTurn

    def isEmpty(self, x,y):
        return self.game[x,y] == 0

    def hasWon(self):
        length = range(3)
        for x in length:
            if self.allEqual(self.game[x,:]) and not self.game[x,1] == 0:
                self.printWon(self.game[x,1])
                return True
            if self.allEqual(self.game[:,x]) and not self.game[1,x] == 0:
                self.printWon(self.game[1,x])
                return True
        if ((self.game[0,0] == self.game[1,1] and self.game[0,0] == self.game[2,2]) or (self.game[0,2] == self.game[1,1] and self.game [2,0] == self.game[1,1])) and not self.game[1,1] == 0:
            self.printWon(self.game[2,2])
            return True
        return False

    def printWon(self, player):
        self.winner = self.translate[player]
        #print(self.winner + " Wins!")

    def allEqual(self, list):
        first = list[0]
        for elem in list:
            if elem != first:
                return False
        return True

    def printGame(self):
        board = " {} | {} | {} \n------------ \n {} | {} | {} \n------------ \n {} | {} | {}"
        arr = self.game.ravel()
        translated = [self.translate[x] for x in arr]
        #print(board.format(*translated))

    def xGoes(self, x,y):
        global isXTurn
        if (not isXTurn) or (not self.isEmpty(x,y)):
            return False
        self.game[x,y] = 2
        return True

    def oGoes(self, x,y):
        global isXTurn
        if isXTurn or (not self.isEmpty(x,y)):
            return False
        self.game[x,y] = 1
        return True

    def hasEnded(self):
        return (self.hasWon() or self.isDraw()) 

    def reset(self):
        self.game = np.zeros((3,3))
        self.winner = "draw"
        global isXTurn 
        isXTurn = True

    def getWinner(self):
        return self.winner

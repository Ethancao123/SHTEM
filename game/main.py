from TTTGame import TTTGame as g
from Player import Player as p
from HumanPlayer import HumanPlayer as h
from RandomPlayer import RandomPlayer as r
import PySimpleGUI as sg
import pickle



numTries = 100000;

def save(obj):
        try:
            with open("data.pickle", "wb") as f:
                pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)

def load(filename):
    objects = []
    with (open(filename, "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects[0]

xWins = 0
oWins = 0
draws = 0

#choose between existing and new object
#p1 = load("C:/Users/ethan/OneDrive/Documents/GitHub/SHTEM/game/data.pickle")
p1 = load("data.pickle")
p2 = load("data.pickle")
#p2 = load("data backup.pickle")
#p1 = SavaData.load()
#p2 = load("C:/Users/ethan/OneDrive/Documents/GitHub/SHTEM/game/data.pickle")
game = g(p1, p2)
for x in range(numTries):
    while(not game.hasEnded()):
        response = game.makeMove()
        if response == -1:
            break
        while response == False:
            response = game.makeMove()
        game.printGame()
    winner = game.getWinner()
    if winner == "draw" or winner == " ":
        p1.reward(-1)
        p2.reward(-1)
        draws += 1
    elif winner == "X":
        p1.reward(10)
        p2.reward(-1)
        xWins += 1
    elif winner == "O":
        p1.reward(-1)
        p2.reward(10)
        oWins += 1
    else:
        print(winner)
    game.reset()
save(p1)
print("game is over")
print("X Wins = " + str(xWins))
print("O Wins = " + str(oWins))
print("draws = " + str(draws))




from TTTGame import TTTGame as g
from Player import Player as p
from HumanPlayer import HumanPlayer as h
from RandomPlayer import RandomPlayer as r
import PySimpleGUI as sg
import pickle
import csv
from alive_progress import alive_bar



numTries = 1000000
refreshRate = 100
testRate = 10

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

def test(game, p1, p2):
    p1Chance = p1.getExploreChance()
    p2Chance = p2.getExploreChance()
    p1.setExploreChance(0)
    p2.setExploreChance(0)
    for x in range(1):
        while(not game.hasEnded()):
            response = game.makeMove()
            if response == -1:
                break
            while response == False:
                response = game.makeMove()
            game.printGame()
        winner = game.getWinner()
        if winner == "draw" or winner == " ":
            global draws 
            draws+= 1
        elif winner == "X":
            global xWins 
            xWins += 1
        elif winner == "O":
            global oWins 
            oWins += 1
        game.reset()
    p1.setExploreChance(p1Chance)
    p2.setExploreChance(p2Chance)

filewriter = None
toCSV = []
#toCSV = [["Iterations", "Wins", "Draws", "Loses"]]
#x is 2, o is 1

xWins = 0
oWins = 0
draws = 0

p1Symbol = 2
p2Symbol = 1
#choose between existing and new object
p1 = load("C:/Users/ethan/OneDrive/Documents/GitHub/SHTEM/data.pickle")
#p1 = p(p1Symbol)
p2 = r(p2Symbol)
p1.setSymbol(p1Symbol)
p2.setSymbol(p2Symbol)
p2.setExploreChance(1)
#p2 = load("data backup.pickle")
#p1 = SavaData.load()
#p2 = load("C:/Users/ethan/OneDrive/Documents/GitHub/SHTEM/game/data.pickle")
game = g(p1, p2)
iterations = 0;
with alive_bar(int(numTries/refreshRate), bar = 'classic', spinner = 'bar_recur') as bar:
    for x in range(numTries):
        iterations += 1
        while(not game.hasEnded()):
            response = game.makeMove()
            if response == -1:
                break
            while response == False:
                response = game.makeMove()
            game.printGame()
        winner = game.getWinner()
        if winner == "draw" or winner == " ":
            p1.reward(-1, game.getBoard())
            # p2.reward(-1)
            # draws += 1
        elif winner == "X":
            p1.reward(10, game.getBoard())
            # p2.reward(-1)
            # xWins += 1
        elif winner == "O":
            p1.reward(-10, game.getBoard())
            # p2.reward(10)
            # oWins += 1
        else:
            print(winner)
        game.reset()
        if(iterations % refreshRate == 0):
            p2.setRewardTable(p1.getRewardTable())
            #p2.invertTable()
            p2.setSymbol(p2Symbol)
            p1.reduceExploreChance()
            bar()
        if(iterations % testRate == 0):
            test(game,p1,p2)
            toCSV.append([iterations, xWins, draws, oWins])
            xWins = 0
            draws = 0
            oWins = 0
with open('data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    count = 0
    total = 0
    for i in toCSV:
        filewriter.writerow(i)
print("game is over")
save(p1)






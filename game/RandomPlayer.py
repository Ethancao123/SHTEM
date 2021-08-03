import random

exploreChance = 1

class RandomPlayer:
    def __init__(self, symbol):
        pass

    def getMove(self, game):
        moves = self.getPossibleMoves(game)
        return random.choice(moves)

    def getRewardTable(self):
        return None
    
    def setRewardTable(self, table):
        pass

    def getExploreChance(self):
        return 1

    def reduceExploreChance(self):
        pass
        
    def setExploreChance(self, chance):
        pass

    def setSymbol(self, symbol):
        pass

    def getPossibleMoves(self, game):
        emptySpaces = []
        for i in range(3):
            for j in range(3):
                if self.isEmpty(game, i, j):
                    emptySpaces.append([i,j])
        return emptySpaces
            

    def isEmpty(self, game, x, y):
        return game[x,y] == 0

    def getHash(self, game):
        return str(game.ravel())
    
    def reward(self, num):
        pass
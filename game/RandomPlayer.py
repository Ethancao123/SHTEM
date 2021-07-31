import random

exploreChance = 1

class RandomPlayer:
    def __init__(self, symbol):
        pass
    def getMove(self, game):
        moves = self.getPossibleMoves(game)
        return random.choice(moves)


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
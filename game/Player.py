import random


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.states = []
        self.stateRewards = {}
        self.exploreChance = 1
        self.learningRate = 0.75
        self.decayGamma = 0.9
    
    def invertTable(self):
        for x in self.stateRewards.keys():
            self.stateRewards[x] *= -1

    def getRewardTable(self):
        return self.stateRewards
    
    def setRewardTable(self, table):
        self.stateRewards = table

    def getExploreChance(self):
        return self.exploreChance

    def reduceExploreChance(self):
        self.exploreChance /= 1.01

    def setExploreChance(self, chance):
        self.exploreChance = chance

    def setSymbol(self, symbol):
        self.symbol = symbol 

    def getMove(self, game):
        moves = self.getPossibleMoves(game)
        if random.random() < self.exploreChance:
            self.states.append(self.getHash(game))
            return random.choice(moves)
        else:
            reward = 10000
            bestMove = moves[0]
            for m in moves:
                future = game.copy()
                future[m[0],m[1]] = self.symbol
                futureHash = self.getHash(future)
                futureReward = self.stateRewards.get(futureHash)
                if futureReward == None:
                    futureReward = 0
                if reward > futureReward:
                    reward = futureReward
                    bestMove = m
        self.states.append(self.getHash(game))
        return bestMove

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
    
    def reward(self, num, g):
        self.states.append(self.getHash(g))
        for state in reversed(self.states):
            if self.stateRewards.get(state) == None:
                self.stateRewards[state] = 1
            self.stateRewards[state] += self.learningRate * (self.decayGamma * num - self.stateRewards[state])
        self.states = []
        if self.exploreChance > 0:
            pass 
            #self.exploreChance - 0.00001
    
    def getRewards(self):
        return self.stateRewards

# make q table copy every 100
# 
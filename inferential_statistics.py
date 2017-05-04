# -*- coding: utf-8 -*-
"""
Created on Wed May  3 07:27:16 2017

@author: KoushikVikram
"""

import random

class FairRoulette():
    ''' This class is called FairRoulette because you have an even 
    chance of winning and losing. '''
    def __init__(self):
        ''' initialize all components of the game - pockets, ball, blackOdds, redOdds, pocketOdds '''
        # initialize pockets 1 through 36
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None    # this denotes where the ball stops
        self.blackOdds, self.redOdds = 1.0, 1.0    # black and red odds. i.e. the value of black and red
        self.pocketOdds = len(self.pockets) - 1.0    # value of pockets. why -1? imagine there were 2
        # pockets instead of 1. In that case, if you choose the right pocket, you should win $1, not $2
        
    # spin the roulette
    def spin(self):
        ''' spin the roulette - chooses a pocket at random and assigns it to self.ball '''
        self.ball = random.choice(self.pockets)
    
    # check if the ball is in black pocket        
    def isBlack(self):
        ''' defines which pockets are black. returns True/False depending on value of ball'''
        if type(self.ball) != int:
            return False
        # this is just the way numbers are laid out on a roulette wheel
        if ((self.ball > 0 and self.ball <= 10) or (self.ball > 18 and self.ball <= 28)):
            return self.ball%2 == 0
        else:
            return self.ball%2 == 1
            
    # check if the ball is in red pocket                
    def isRed(self):
        ''' defines which pockets are red. 
        If it's not black, it must be red'''
        return type(self.ball) == int and not self.isBlack()
    
    # you can bet black
    def betBlack(self, amt):
        ''' returns amount won/lost by betting on black: positive or negative number '''        
        if self.isBlack():
            return amt*self.blackOdds
        else: 
            return -amt

    # you can bet red
    def betRed(self, amt):
        ''' returns amount won/lost by betting on red: positive or negative number '''        
        if self.isRed():
            return amt*self.redOdds
        else:
            return -amt*self.redOdds
    
    # you can bet a number    
    def betPocket(self, pocket, amt):
        ''' returns amount won/lost by betting on pocket: positive or negative number '''        
        # if the ball has stopped at the pocket        
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds    # return amount times the value of self.pocketOdds
        # ohterwise, you lose your amount    
        else:
            return -amt
            
    def __str__(self):
        return 'Fair Roulette'


# simulation
def playRoulette(game, numSpins, toPrint = True):
    ''' game:type of game, numSpins:int, toPrint:Boolean -> expected returns (red:float, black:float, pocket:float)'''    
    luckyNumber = '2'    # this is the number we choose to bet on
    bet = 1    # this is the amount we bet
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0    # initialize amount won from red, black and pocket
    # Spin the wheel numSpins times and add to the amounts won from betting red, black and pocket    
    for i in range(numSpins):
        game.spin()
        # we bet on all 3 possibilities - red, black and pocket(in this case, 2)
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, ' spins of ', game)
        print('Expected return betting red = ', str(100*totRed/numSpins) + '%')
        print('Expected return betting black = ', str(100*totBlack/numSpins) + '%')
        print('Expected return betting ', luckyNumber, '= ', str(100*totPocket/numSpins) + '%\n')
    return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)

'''
numSpins = 10000000
game = FairRoulette()
playRoulette(game, numSpins)    # the expected answer for all three cases is close to zero, since
                                # since each case has an equal probability of occuring and not occuring
                                # therefore, the gains and losses should even out
'''

class EuRoulette(FairRoulette):
    ''' EuRoulette is a biased Roulette with an extra pocket for '0'.
    EuRoulette inherits from FairRoulette. '''
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    ''' AmRoulette is a biased Roulette with extra pockets for '0' and '00'.
    AmRoulette inherits from EuRoulette. '''
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return 'American Roulette'

# function to get just the returns from pockets        
def findPocketReturn(game, numTrials, trialSize, toPrint):
    '''game:type of game, numTrials:int, trialSize:numSpins(int), toPrint:Boolean -> pocketReturns:[float]
    returns a list of amounts won/lost when the Roulette is spun numTrials times.'''
    pocketReturns = []
    # play Roulette numTrials times
    for t in range(numTrials):
        # store the results of playing the game. this is a tuple of 3 floats - red, black and pocket
        trialVals = playRoulette(game, trialSize, toPrint)
        # append the amount won/lost from pockets to pocketReturns        
        pocketReturns.append(trialVals[2])
    return pocketReturns
    

'''
random.seed(0)
numTrials = 20
resultDict = {}    # maps a game to a list of results for that game
games = {FairRoulette, EuRoulette, AmRoulette}

# assign the game names as keys to resultDict and initialize each with an empty list
for G in games:
    resultDict[G().__str__()] = []

# spin different number of times
for numSpins in (100, 1000, 10000, 100000):
    print('\n Simulate betting a pocket for ', numTrials, ' trials ', numSpins, ' spins each.')
    # calculate pocketReturns for each game with numSpins spins    
    for G in games:
        pocketReturns = findPocketReturn(G(), numTrials, numSpins, False)
        # print the % mean of expected return
        print('Exp. return for ', G(), '=', str(100*sum(pocketReturns)/float(len(pocketReturns))) + '%')
'''


def getMeanAndStd(X):
    ''' X:(float) -> mean:float, std:float
    returns mean and standard deviation of the sample set X '''
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
    
''' Empirical rule:
- ~68% of data within 1 standard deviation of mean
- ~95% of data within 1.96 standard deviations of mean
- ~99.7% of data within 3 standard deviations of mean '''

'''
# Applying empirical rule
numTrials = 20
resultDict = {}
games = (FairRoulette, EuRoulette, AmRoulette)
# assign the game names as keys to resultDict and initialize each with an empty list 
for G in games:
    resultDict[G().__str__()] = []
for numSpins in (100, 1000, 10000):
    print('\n Simulate betting a pocket for ', numTrials, ' trials of ', numSpins, ' spins each.')
    for G in games:
        # calculate pocket returns for game G with numSpins spins
        pocketReturns = findPocketReturn(G(), 20, numSpins, False)
        # calculate mean and standard deviation of pocketReturns
        mean, std = getMeanAndStd(pocketReturns)
        resultDict[G().__str__()].append((numSpins, 100*mean, 100*std))
        print('Exp. return for ', G(), ' = ', str(round(100*mean, 3)) + '%, ', '+/- ' + 
        str(round(100*1.96*std, 3)) + '% with 95% confidence')
'''        

# Distributions
# Generating normal distributions
import pylab
dist = []
for i in range(100000):
    dist.append(random.gauss(0, 30))
pylab.hist(dist, 30)

# Checking empirical rule
import scipy.integrate

def gaussian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-( ( (x - mu)**2) / (2*sigma**2) )
    return factor1*factor2
    
def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu = ', mu, 'and sigma = ', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian, mu-numStd*sigma, mu+numStd*sigma, (mu, sigma))[0]
            print('Fraction within ', numStd, 'std = ', round(area, 4))

# checkEmpirical(3)

# note that the empirical rule applies only to normal distributions



        
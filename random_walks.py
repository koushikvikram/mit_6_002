#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 09:24:33 2017

@author: koushikvikram
"""

# random walks

'''
Structure of a simulation:
1. Simulate on walk of k steps
2. simulate n such walks
3. report average distance from origin
'''

'''
First, some useful abstractions
1. Location - a place
2. Field - a collection of places and drunks
3. Drunk - somebody who wanders from place to place in a field
'''

# Location class - representing a place
class Location(object):
    def __init__(self, x, y):    # Design decision 1 - Our location is two dimensional. 
        '''x:float, y:float'''   # So, we only have x and y coordinates
        self.x = x
        self.y = y

    # use the move method to get the new Location 
    def move(self, deltaX, deltaY):    # Design decision 2 - making deltaX and deltaY floats, gives 
        '''deltaX:float, deltaY:float'''    # us a richer notion of location
        return Location(self.x + deltaX, self.y + deltaY)   # the new Location is returned
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        '''other:Location(x,y) -> distance of other from current location'''
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5    # pythagorean theorem
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
        

# Field class - a collection of places and drunks
class Field(object):
    ''' the key design decision embodied in this implementation is
    to make the location of a drunk in a field an attribute of the field
    rather than an attribute of the drunk. 
    - We think of a field as a mapping from drunks to locations
    This decision puts a constraint on how we can implement the class drunk
    - Since I'm using drunks as keys in a dict, it tells me that the type drunk
    will have to be hashable.'''
    def __init__(self):
        self.drunks = {}    # representing the field as dict - a mapping from drunks to locations
                            # therefore, the type 'drunk' has to be hashable
        
    def addDrunk(self, drunk, loc):
        ''' add a drunk to the field'''
        # Design decision - check to see if the drunk is already in the field. 
        # Therefore, we are not allowing a drunk to be cloned. 
        if drunk in self.drunks:   
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[drunk] = loc
                       
    def getLoc(self, drunk):
        ''' get the location of the drunk in the field '''
        # check to see if the drunk is on the field
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]
    
    def moveDrunk(self, drunk):
        ''' move the drunk by one step and update the location of the drunk.'''
        # Design Decision - check if the drunk is on the field - Defensive programming.
        # I could have assumed that the drunk is already on the field, but because a field is 
        # represented as a dicttionary, it is reasonably efficient to check if a drunk is already
        # in the set of keys
        if drunk not in self.drunks:   
            raise ValueError('Drunk not in field')
        # see how far the drunk has moved in each direction
        xDist, yDist = drunk.takeStep()    
        currentLocation = self.drunks[drunk]
        # use move method to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
    
''' 
notable aspects of the Class Field:
    - A mapping of drunks to locaions
    - Unbounded size
    - Allows multiple drunks
        - with no constraints about how they relate to each other
        - eg. two drunks can occupy the same location
'''

# Drunk class - somebody who wanders from place to place in a field
class Drunk(object):
    ''' This class is not intended to be useful on its own.
    This is a base class to be inherited. '''
    def __init__(self, name = None):
        self.name = name
    
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
        

# two subclasses of drunks - we implement two types of drunks
import random

class UsualDrunk(Drunk):
    ''' UsualDrunk moves one unit east, west, north or south, each with equal probability '''
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    ''' wants to get away from the cold. So, takes a shorter step nortwards and longer step southwards. 
    ColdDrunk can take a step in any direction with equal probability '''
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

# Simulating a walk

# 1.simulating a single walk
def walk(f, d, numSteps):
    ''' f:Field, d:Drunk, numSteps:int>=0 -> distance covered
    moves d numSteps times;
    returns the distance between the final location and the location at the start of the walk. '''
    # record the starting location
    start = f.getLoc(d)
    # move d numSteps times
    for s in range(numSteps):
        f.moveDrunk(d)
    # return the distance between the final location and starting location
    return start.distFrom(f.getLoc(d))
# the above code is so simple because we first took the trouble to find some useful data abstractions 

# 2.simulating multiple walks
def simWalks(numSteps, numTrials, dClass):
    ''' numSteps:int>=0, numTrials:int>0, dClass:subclass of Drunk -> distances:[float]
    - simWalks has an argument dClass so that we can simulate the walks of many different kinds of drunks
    Simulates numTrials walks of numSteps steps each.
    Returns a list of the final distances for each trial.'''
    # create a drunk
    Homer = dClass()
    # create the origin. The drunk will start walking from here
    origin = Location(0,0)
    # initialize distances to record the distance covered by the drunk on each trial
    distances = []
    # run numTrials trials
    for t in range(numTrials):
        # for each trial: 
        # create a new field
        f = Field()
        # put the drunk on the field 
        f.addDrunk(Homer, origin)
        # walk the drunk numSteps steps and append the distance covered to the distances list
        distances.append(round(walk(f, Homer, numSteps), 1))
    # return the distances list
    return distances

# 3.report aggregated results
def drunkTest(walkLengths, numTrials, dClass):
    ''' walkLengths:(numSteps:int>0), numTrials:int>0, dClass:subclass of Drunk
    For each number of steps in walkLengths, run simWalks with numTrials walks
    and print results '''
    # for each walkLength
    for numSteps in walkLengths:
        # simulate the walk numTrials times, get and store the distances
        distances = simWalks(numSteps, numTrials, dClass)
        # print the type of drunk, number of steps, the mean, the minimum and maximum distance covered
        print(dClass.__name__, 'random walk of ', numSteps, ' steps')
        print('Mean = ', round(sum(distances)/len(distances) ,4))
        print('Max = ', max(distances), 'Min = ', min(distances))

# simulate drunkTest for multiple types of drunks
def simAll(drunkKinds, walkLengths, numTrials):
    ''' drunkKinds:(Drunk), walkLengths:(numSteps:int>0), numTrials:int>0'''
    # for each type of Drunk in drunkKinds, run drunkTest
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)
        
random.seed(0)
# drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
# simAll((UsualDrunk, ColdDrunk), (1, 10, 100, 1000, 10000), 100)

# sanity check
#drunkTest((0, 1, 2), 100, UsualDrunk)

import pylab

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles =styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of ', numSteps, ' steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def simAllPlot(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of ', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
    pylab.title('Mean Distance from origin (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')

# numSteps = (10, 100, 1000, 10000)
# simAllPlot((UsualDrunk, ColdDrunk), numSteps, 100)

def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        meanX = sum(abs(xVals))/len(xVals)
        meanY = sum(abs(yVals))/len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = dClass.__name__ + ' mean abs dist = <' + str(meanX) + ', ' + str(meanY) + '>')
    pylab.title('Location at End of Walks (' + str(numSteps) + ' steps')
    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.ylabel('Steps North/South of Origin')
    pyla.xlabel('Steps East/West of Origin')
    pylab.legend(loc = 'upper left')

# plotLocs((UsualDrunk, ColdDrunk), 10000, 1000)

class OddField(Field):
    def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x,y)] = newLoc

    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]


def traceWalk(fieldKinds, numSteps):
    styleChoice =styleIterator(('b+', 'r^', 'ko'))
    for fClass in fieldKinds:
        d = UsualDrunk()
        f = fClass()
        f.addDrunk(d, Location(0, 0))
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = fClass.__name__)
    pylab.title('Spots Visited on Walk (' + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'best')

# traceWalk((Field, OddField), 500)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:38:02 2017

@author: koushikvikram
"""

# stochastic processes

"""
# underdetermined function - may or may not return random number 
def rollDie():
    ''' returns an int between 1 and 6'''

# Stochastic process - requires randomness    
def rollDie():
    ''' returns a randomly chosen int between 1 and 6'''

# non-deterministic function - specification allows randomness but does not require it    
def squareRoot(x, epsilon):
    '''Assumes x and epsilon are of type float
    x >= 0 and epsilon > 0
    Returns float y such that x-epsilon <= y*y <= x+epsilon'''
"""    

# implementing a random process

import random

def rollDie():
    '''returns a random int between 1 and 6'''
    return random.choice([1,2,3,4,5,6])    
    # given a sequence of elements, random.choice returns some random 
    # element of it with equal probability
    
def testRoll(n=10):
    ''' n:num(default=10) - number of die rolls -> result: str - outcome of the n rolls in order
    rolls a die n times and returns the outputs'''
    result = ''    # initialize result
    for i in range(n):    # repeat n times  
        result = result + str(rollDie())    # roll the die and append output to result
    print(result)
    
# testRoll()

def genEven():
    '''Returns a random even number x, where 0 <= x < 100 '''
    return random.randrange(0,100,2)
    
def deterministicNumber():
    ''' Deterministically generates and returns an even number betweeen 9 and 21 '''
    return 10    # or 12 or 14 or 16 or 18 or 20
    
def stochasticNumber():
    ''' Stochastically generates and returns a uniformly distributed even number 
    between 9 and 21 '''
    return random.randrange(10,21,2)    # random.randrange() returns a randomly selected element from range
    # random.randrange() generates equally distributed values
    
# the following two distributions are equivalent 
# random.random() is a uniform distribution over [0.0, 1.0)
# dist1() and dist2() are uniform distributions over [-1.0,1.0)
def dist1():
    return random.random()*2 - 1
    
def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1
        
# the following two distributions are equivalent
# both random.random() and random.randrange() are uniform distributions 
# dist3 and dist4 are discrete uniform distributions over [0,1,2,3,4,5,6,7,8,9]
def dist3():
    return int(random.random()*10)
    
def dist4():
    return random.randrange(0,10)
    
# the following two distriutions are NOT equivalent
# both random.random() and random.randint() are uniform distributions
# however, random.randint(start,end) is inclusive of both the start and end points 
# unlike random.randrange(start,end)
def dist5():
    return int(random.random()*10)
    
def dist6():
    return random.randint(0,10)

# to get a better understanding of these distributions, try the following commands:
'''
import pylab as plt
plt.hist([dist1() for n in range(100000000)])    # 100 million times
plt.hist([dist2() for n in range(100000000)])
plt.hist([dist3() for n in range(100000000)])
plt.hist([dist4() for n in range(100000000)])
plt.hist([dist5() for n in range(100000000)])
plt.hist([dist6() for n in range(100000000)])
'''
    
# a simulation to calculate probability
def runSim(goal, numTrials):
    ''' goal:str (expected dice output), numTrials:num (number of times the die is rolled)
    This simulation is run to calculate the probability of getting the expected output(goal)
    when the experiment is performed 'numTrials' times.
    Also, the actual probability of getting the output is calculated.'''
    total = 0    # intialize total - the number of times the output has been achieved
    # perform the experiment numTrials times
    for i in range(numTrials):
        result = ''    # initialize result - the string in which we record the outputs
        # for each experiment, roll the die len(goal) times
        for j in range(len(goal)):
            result += str(rollDie())    # append the outcome to the result
        # if the expected output is got, increase total by 1
        if result == goal:    
            total += 1
    # the probability of any outcome when a die is rolled n times is 1/(6**n)  
    print('Actual Probability = ', round(1/(6**len(goal)),8) )
    # the calculated probability is the number of occurences/ number of trials
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability = ', round(estProbability, 8))
    
# runSim('11111', 1000000)

def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests
    
print('Frequency of double 6 = ', str(fracBoxCars(100000)*100) + '%')

def twoTenDice():
    d1 = [n for n in range(1,11)]
    d2 = [n for n in range(1,11)]
    sampleSpace = []
    for i in d1:
        for j in d2:
            sampleSpace.append([i,j])
    return sampleSpace
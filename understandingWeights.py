#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:18:21 2017

@author: koushikvikram
"""

# understanding weights in np.hist()

# in the usual histogram, the size of each bin is determined solely by the number of elements contained in that bin
# in this case, we want each bin to show the probability of the mean falling within that bin - done using the weights keyword
# the argument, weights, is bound to an array of the same length as the first argument to hist and is used to assign a weight
# to each element in that first argument
# therefore, in the resulting histogram, each value in a bin contributes its associated weight towards the bin count 
# instead of the usual one 
# eg. assuming len(mean) = 5, pylab.array(5*[1])/5 -> array([ 0.2,  0.2,  0.2,  0.2,  0.2])

# let's run an experiment to understand weights
# consider the population (all outcomes that can occur) to be numbers between 1 and 6 
population = [1,2,3,4,5,6]

# let the outcomes that occured be [1, 1, 2, 3, 5, 6]
outcomes = [1,1,2,3,5,6]

# let's assume that each outcome in the population has an equal probability of occuring
assumedProbabilities = dict()
for num in population:
    assumedProbabilities[num] = 1/float(len(population))
    
# now, let's count the number of occureneces of each outcome
numOccurences = dict()
# - initialize number of occurences of each element in population to 0 i.e. we still haven't started counting
for num in population:
    numOccurences[num] = 0

# - count the number of occurences                  
for outcome in outcomes:
    numOccurences[outcome] += 1
    

# let's calculate the observed probability                 
# observed probability = number of occurences* assumed probability
observedProbabilities = dict()
for num in population:
    observedProbabilities[num] = assumedProbabilities[num]*numOccurences[num]

# thus, setting weights displays a histogram with the probability of occurence of each outcome, rather than the count of 
# each outcome

print('The considered population is ', str(population), '\n')
print('The outcomes are: ', str(outcomes), '\n')
print('The assumed probabilites are: ', str(assumedProbabilities), '\n')
print('The number of occrences of each outcome: ', str(numOccurences), '\n')
print('The observed probability is the product of number of occurences of each element \n and its assumed probability ', 
      observedProbabilities)
    






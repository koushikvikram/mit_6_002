#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:37:56 2017

@author: koushikvikram
"""

# Knapsack problem - Greedy algorithm

# Step 1: represent the items by a pair, <value, weight>
# Data abstraction
class Food(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'


# Step 2: Helper function.
# Build a menu of foods
def buildMenu(names, values, calories):
    ''' name:[strings], values:[numbers], calories:[numbers] -> menu:[Food] '''
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i],values[i],calories[i]))
    return menu


# Step 3: Flexible Greedy algorithm.
# while Knapsack is not full, put the best available item in the Knapsack
# The parameter keyFunction makes our implementation independent of the definition of best
# This makes the algorithm flexible
def greedy(items, maxCost, keyFunction):
    """ items:[item], maxCost:num>=0, keyFunction:item.function -> result:[item]
	while maxCost has not been reached, add the most valuable item available
    """
    # sort the items, most valuable first
    itemsCopy = sorted(items, key = keyFunction, reverse = True) 
    # Note that we are using the sorted function as we want the original
    # items list unaltered. Also, reverse = True sorts items from best to worst
    
    # initialize result
    result = []
    # initialize totalValue and totalCost
    totalValue, totalCost = 0.0, 0.0
    
    # iterate throught the list of items
    for i in range(len(itemsCopy)):
    	# if the total value of items is lesser than maxCost
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
        	# take the item i.e. update result 
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()    # update totalCost
            totalValue += itemsCopy[i].getValue()    # update totalValue    
            
    return (result, totalValue)


# Testing our greedy algorithm
def testGreedy(items, constraint, keyFunction):
	taken, val = greedy(items, constraint, keyFunction)
	print('Total value of items taken =', val)
	for item in taken:
		print(item)


# Using our greedy algorithm
def testGreedys(foods, maxUnits):
	print('Use Greedy by value to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.getValue)

	print('\n Use Greedy by cost to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, lambda x:1/Food.getCost(x))

	print('\n Use Greedy by density to allocate', maxUnits, 'calories')
	testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]

foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
testGreedys(foods, 1000)
testGreedys(foods, 800)



    
    
    
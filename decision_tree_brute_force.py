class Food(object):
    def __init__(self, n, v, w):
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
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of Items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def maxVal(toConsider, avail):
	""" Assumes toConsider a list of items, avail a weight (cost)
	Returns a tuple of the total value of a solution to the
	0/1 knapsack problem and the items of that solution. 
	Loosely structured around a decision tree. 
	Local variable result records the best solution found so far. 
	With cost as a constraint, get maximum valued items """

	if toConsider == [] or avail == 0:
		result = (0,())
	elif toConsider[0].getCost() > avail:
		# Explore the right branch
		result = maxVal(toConsider[1:], avail)
	else:
		nextItem = toConsider[0]
		# Explore left branch
		withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
		withVal += nextItem.getValue()
		# Explore right branch
		withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
		# Choose better branch
		if withVal > withoutVal:
			result = (withVal, withToTake + (nextItem,))
		else:
			result = (withoutVal, withoutToTake)
	return result

def maxVal(toConsider, avail):
	if toConsider == [] or avail == 0:
		return (0,())
	elif toConsider[0].getCost() > avail:
		result = maxVal(toConsider[1:],avail)
	else:
		nextItem = toConsider[0]
		withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
		withVal += nextItem.getValue()

		withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

		if withVal > withoutVal:
			result = (withVal, withToTake + (nextItem,))
		else:
			result = (withoutVal, withoutToTake)
		return result
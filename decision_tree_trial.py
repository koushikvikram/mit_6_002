def maxVal(toConsider, avail):
	''' toConsider:[item], avail:num -> result:(value:num, items:(item)) 
	objective - choose a combination of items that give us maximum value
	within the given constraint ie. avail (cost of item)
	result is the total value of items chosen and a tuple of items chosen
	algorithm : decision tree - take/leave each item, explore consequence
	notes: recursive function
	 '''

	# base case - empty list of items or avail = 0 -> nothing to choose from, value is 0

	# optimization - if the cost of item considered is greater than constraint, ignore it and compute with remaining items 

	# recursive case - consider left branch and right branch, subject to constraint
	
	# left branch - take item. 
	# Consequence - update value of items chosen, update constraint. 
	# Consider the remaining items

	# right branch - leave out item.
	# Consequence - none 
	# Consider the remaining items

	# find the branch that has more value and assign it to result 

	return result

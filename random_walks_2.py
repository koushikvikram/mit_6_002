# random walks

# simulation:
# 1. simulate a single walk
# 2. simulate multiple walks
# 3. report the aggregate results

# data abstractions
class Location(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, deltaX, deltaY):
		return Location(self.x + deltaX, self.y + deltaY)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def distFrom(self, other):
		ox = other.x
		oy = other.y
		distX = ox - self.x
		distY = oy - self.y
		return ((distX**2 + distY**2)**0.5)    # pythagorean theorem

	def __str__(self):
		return '< ' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
	def __init__(self):
		self.drunks = {}

	def addDrunk(self, drunk, loc):
		if drunk in self.drunks:
			raise ValueError('Duplicate Drunk.')
		else:
			self.drunks[drunk] = loc

	def getLoc(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field.')
		else:
			return self.drunks[drunk]

	def moveDrunk(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		xDist, yDist = drunk.takeStep()
		currentLocation = self.drunks[drunk]
		self.drunks[drunk] = currentLocation.move(xDist, yDist)

class Drunk(object):
	def __init__(self, name = None):
		self.name = name

	def __str__(self):
		if self != None:
			return self.name
		return 'Anonymous'

import random
class UsualDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
		return random.choice(stepChoices)

class ColdDrunk(Drunk):
	def takeStep(self):
		stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
		return random.choice(stepChoices)

# simulation
def walk(f, d, numSteps):
	start = f.getLoc(d)
	for step in range(numSteps):
		f.moveDrunk(d)
	return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
	Homer = dClass()
	origin = Location(0, 0)
	distances = []
	for trial in range(numTrials):
		f = Field()
		f.addDrunk(Homer, origin)
		distance = round(walk(f, Homer, numSteps), 1)
		distances.append(distance)
	return distances

def drunkTest(walkLengths, numTrials, dClass):
	for numSteps in walkLengths:
		distances = simWalks(numSteps, numTrials, dClass)
	print(dClass.__name__, 'random walk of ', numSteps, 'steps')
	print('Mean = ', round(sum(distances)/len(distances), 4))
	print('Max = ', max(distances), ' Min = ', min(distances))

def simAll(drunkKinds, walkLengths, numTrials):
	for dClass in drunkKinds:
		drunkTest(walkLengths, numTrials, dClass)

random.seed(0)
# drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
simAll((UsualDrunk, ColdDrunk), (1, 10, 100, 1000, 10000), 100)

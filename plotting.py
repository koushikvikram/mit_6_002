#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:46:39 2017

@author: koushikvikram
"""

# Plotting
import pylab as plt

# most basic function in PyLab - plots two lists as x and y values

# first, let's generate some example data
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
# to generate a plot, call
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

# we would like to graph each one separately
# calling plt.figure(<arg>) will create a new plot with the name <arg> 
# When I call plt.figure without arguments for the first time, it will generte a new display
# with that name. If a display already exists with that name, it will reopen it and let me
# do additional processing inside of it
plt.figure('lin')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.plot(mySamples, myQuadratic)

plt.figure('cubic')
plt.plot(mySamples, myCubic)

plt.figure('expo')
plt.plot(mySamples, myExponential)

# making changes to the figure
# note that you have to call the figure first before making changes to it
# adding xlabels and ylabels to the figures
plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')

plt.figure('quad')
plt.xlabel('sample points')
plt.ylabel('quadratic function')

plt.figure('cubic')
plt.xlabel('sample points')
plt.ylabel('cubic function')

plt.figure('expo')
plt.xlabel('sample points')
plt.ylabel('exponential function')

# adding titles to the figures
plt.figure('lin')
plt.title('Linear')

plt.figure('quad')
plt.title('Quadratic')

plt.figure('cubic')
plt.title('Cubic')

plt.figure('expo')
plt.title('Exponential')

# notice that in each figure, the color of the plot is the same
# at the same time, although we have called the figure with just the title,
# we still see the xlabel and ylabel on it
# this is because the figures are created in the same frame


# clearing frames using the plt.clf() function
plt.figure('lin')
plt.clf()
plt.plot(mySamples, myLinear)
plt.title('Linear')

plt.figure('quad')
plt.clf()
plt.plot(mySamples, myQuadratic)
plt.title('Quadratic')

plt.figure('cubic')
plt.clf()
plt.plot(mySamples, myCubic)
plt.title('Cubic')

plt.figure('expo')
plt.clf()
plt.plot(mySamples, myExponential)
plt.title('Exponential')


# In the above figures,it is hard to clearly distinguish between the linear and quadratic plots
# This is because the scales on the y-axes are different 
# Lets set limits on the y-axes for both the plots
plt.figure('lin')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myQuadratic)

plt.figure('cubic')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myCubic)

plt.figure('expo')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myExponential)

# overlaying plots - call two plots within the same window/frame
plt.figure('lin quad')
plt.clf()
# plt.ylim(0,1000)
plt.plot(mySamples, myLinear, label='Linear')
plt.plot(mySamples, myQuadratic, label='Quadratic')
plt.legend(loc='upper left')    # give pylab the legend command for it to display the plot labels

plt.figure('cube exp')
plt.clf()
# plt.ylim(0,1000)
plt.plot(mySamples, myCubic, label='Cubic')
plt.plot(mySamples, myExponential, label='Exponential')
plt.legend()    # we let pylab decide where to put the legend

plt.figure('lin quad')
plt.title('Linear vs. Quadratic')

plt.figure('cube exp')
plt.title('Cubic vs. Exponential')


# Changing data display - specifying color, shape and linewidth
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)    # 1st letter in string: color, 2nd: shape
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs Quadratic')

plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=4.0)
plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=5.0)
plt.legend()
plt.title('Cubic vs Exponential')


# Using subplots
# top-down
plt.figure('lin quad')
plt.clf()
plt.subplot(211)    # 2 - # of rows, 1 - # of columns, 1 - location
plt.ylim(0,900)
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)    # 1st letter in string: color, 2nd: shape
plt.subplot(212)
plt.ylim(0,900)    # 2 - # of rows, 1 - # of columns, 2 - location
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs Quadratic')

# side-by-side
plt.figure('cube exp')
plt.clf()
plt.subplot(121)    # 1 row, 2 columns, location 1
plt.ylim(0,140000)
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=4.0)
plt.subplot(122)    # 1 row, 2 columns, location 2
plt.ylim(0, 140000)
plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=5.0)
plt.legend()
plt.title('Cubic vs Exponential')

# Changing scales
plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=4.0)
plt.yscale('log')  # changing to log scale
plt.legend()
plt.title('Cubic vs. Exponential')

plt.figure('cube exp linear')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=4.0)
plt.legend()
plt.title('Cubic vs. Exponential')

 








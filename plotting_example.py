#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:05:16 2017

@author: koushikvikram
"""

# plotting example

# Compound interest formula: A = P(1 + r/n)**(n*t)
# A - Amount, P - Principal, r - annual rate of interest, 
# n - number of times interest is compounded per year, t - # years the amount is deposited/borrowed for

# Example: Planning for retirement
# intend to save an amount 'm' each month
# expect to earn a percentage r of income on investments each month
# want to explore how big a retirement fund will be compounded by the time ready to retire
import pylab as plt


def retire(monthly, rate, terms):
    ''' monthly:num - amount I am going to save each month
    rate(r):num - interest rate (percentage)
    terms(n*t):num - number of terms for which I am going to earn interest
    - this function calculates the compound interest over a term, with monthly savings
    added each month'''
    savings = [0]    # y-axis
    base = [0]    # x-axis
    mRate = rate/12    # monthly rate i.e. r/n
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate) + monthly]    # savings[-1] is the principal. Each month, we add
                                                        # the amount 'monthly' to the account
    return base, savings
    
def displayRetireWMonthlies(monthlies, rate, terms):
    '''monthlies:[nums] - a list of amount saved each month
    rate:num - interest rate per annum
    terms:num - number of terms over which we want to calculate
    - this function plots the amount saved(with interest) over time'''
    plt.figure('retireMonth')
    plt.clf()    # clear frame so that we can reuse the function
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label='retire: '+str(monthly))
        plt.legend(loc='upper left')
        
displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40*12)

def displayRetireWRates(month, rates, terms):
    ''' month:num - monthly saving, rates:[num] - different rates of interest, terms:num - time 
    - this function plots the savings over time for different interest rates'''
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label='retire: '+ str(month) + ':' + str(int(rate*100)))
        plt.legend(loc='upper left')
        
displayRetireWRates(800, [.03, .05, .07], 40*12)

'''
def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)    # limiting the x-axis between 30*12 and 40*12
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, label='retire:'+str(monthly)+':'+str(int(rate*100)))
            plt.legend(loc='upper left')
            
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)
'''
# the above function makes it hard to distinguish plots because of overlap of many graphs
# could just analyze separately
# but can also try to visually separate effects

# cleaning up the displayRetireWMonthsAndRates function
def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel+rateLabel, label='retire:'+str(monthly)+':'+str(int(rate*100)))
            plt.legend(loc='upper left')
            
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)
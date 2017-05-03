#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:37:16 2017

@author: koushikvikram
"""

def ringIndexing(numRange, listLen):
    ''' numRange:int, listLen:int ->  out:[int]
    generates a list of indexes of length numRange
    indexes take values in range(0, listLen) '''
    index = 0
    out = []
    for i in range(numRange):
        out.append(index)
        if index == listLen - 1:
            index = 0
        else:
            index += 1
    return out

out = ringIndexing(10, 3)
print(out)
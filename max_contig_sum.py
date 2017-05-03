#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:31:49 2017

@author: koushikvikram
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    
    power_set = [[]]
    for item in L:
        power_set.extend([subset+[item] for subset in power_set])
        
    str_subsets = {''.join(map(str,subset)):subset for subset in power_set}
    str_L = ''.join(map(str, L))
    
    contig_subsets = [str_subsets[contig] for contig in str_subsets if contig in str_L]
    
    sum_contigs = [sum(contig) for contig in contig_subsets]
    
    return max(sum_contigs)

# not a perfect solution
# fails for the case max_contig_sum([3,-3,3,-3])
# expected output -> 3
# generated ouput -> 6
# since we use the 'in' function for string, 33 in -33 will return true, although this is not the required behavior
# run the code in pythontutor for more clarity 

    
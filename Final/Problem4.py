# -*- coding: utf-8 -*-
"""
Created on 2017-03-13

@author: ac2sherry
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here
    # increasing
    L_max_inc = [L[0]]
    L_max_dec = [L[0]]
    L_max_incloc = 0
    L_max_decloc = 0
    L_max_inctmp = [L[0]]
    L_max_dectmp = [L[0]]
    for idx in range(1,len(L)):			
        if L[idx] > L[idx - 1]:
            # find the temp longest increasing monotonical
            L_max_inctmp.append(L[idx])
            L_max_dectmp = [L[idx]]
        elif L[idx] < L[idx - 1]:
            # find the temp longest decreasing monotonical
            L_max_dectmp.append(L[idx])
            L_max_inctmp = [L[idx]]
        else:
            # if equal both are monotonical
            L_max_inctmp.append(L[idx])
            L_max_dectmp.append(L[idx])
        
#        print(L_max_inctmp)
#        print(L_max_dectmp)
                
        if len(L_max_inc)<len(L_max_inctmp):
            # comparing with longest and temp longest increasing
            L_max_inc = L_max_inctmp.copy()
            L_max_incloc = idx-len(L_max_inctmp)
        if len(L_max_dec)<len(L_max_dectmp):
            # comparing with longest and temp longest decreasing
            L_max_dec = L_max_dectmp.copy()
            L_max_decloc = idx-len(L_max_dectmp)
    
    # comparing with longest increasing and decreasing
    if len(L_max_inc)>len(L_max_dec):
        L_max = L_max_inc
    elif len(L_max_inc)<len(L_max_dec):
        L_max = L_max_dec
    # if they are equal length, find the first occurance one
    elif L_max_incloc <= L_max_decloc:
        L_max = L_max_inc
    elif L_max_incloc > L_max_decloc:
        L_max = L_max_dec
        
    return sum(L_max)
        
L = [1,2,3,4,5]
print(longest_run(L))










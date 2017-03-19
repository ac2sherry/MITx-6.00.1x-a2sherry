# -*- coding: utf-8 -*-
"""
Created on 2017-03-13

@author: ac2sherry
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    if int(us_num) <= 10:
        # less than 10 (个位数)
        result = trans[us_num]
    elif int(us_num) <= 19:
        # less than 19 (十几)
        result = trans['10'] + " " + trans[us_num[-1]]
    elif int(us_num) % 10 == 0:
        # can be divided by 10 (整十的)
        result = trans[us_num[0]] + " " + trans['10']
    else:
        # others
        result = trans[us_num[0]] + " " + trans['10'] + " " + trans[us_num[-1]]
    return result
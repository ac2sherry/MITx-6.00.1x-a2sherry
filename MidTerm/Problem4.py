def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exponent = 0
    while base**exponent <= num:
        exponent += 1
    if abs(base**exponent - num) < abs(base**(exponent-1) - num):
        return exponent
    else:
        return exponent - 1
    
    
print(closest_power(4,1))
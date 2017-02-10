def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0 and len(char) != 0:
        return False
    idx = len(aStr) // 2
    if char == aStr[idx]:
        return True
    elif len(aStr) == 1:
        return False
    elif char > aStr[idx]:
        return isIn(char,aStr[idx:])
    else:
        return isIn(char,aStr[:idx])
    
    
print(isIn('d', 'acdeopqsty'))
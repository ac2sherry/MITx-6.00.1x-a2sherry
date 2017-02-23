def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if isinstance(aList,list):
        return [x for aElement in aList for x in flatten(aElement)]
    else:
        return [aList]

def flatten_re(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if isinstance(aList,list):
        for aElement in aList:
            return flatten_re(aElement)
    else:
        return [aList]

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(aList))
print(flatten_re(aList))
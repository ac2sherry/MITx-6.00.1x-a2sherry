def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    result = 0
    for idx in range(len(listA)):
        result += listA[idx] * listB[idx]
    return result
    
print(dotProduct([1,2,3],[4,5,6]))